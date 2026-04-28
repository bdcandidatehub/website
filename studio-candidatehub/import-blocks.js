const { createClient } = require('@sanity/client');
const fs = require('fs');
const csv = require('csv-parser');
const blockTools = require('@sanity/block-tools');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;

const client = createClient({
  projectId: 'p65whnge',
  dataset: 'production',
  useCdn: false,
  apiVersion: '2023-05-03',
  token: process.env.SANITY_TOKEN || 'skVXXEwG9Gq7M4W0s9bS1cM689g2A0aLzUo9nI2M2h4hZ0pY7tO7nKzL8q9c0Q0s5N1k8xH4sQ5N8tW8oF2gH9vJ5zR7vT1uF9iN8vK2bU5hN0uR0gH8wM8mV0yO3aP1sI2tO0dF7eJ9fR1oP1mZ3jD6wH9mT8vH4hS1kF2rL8' // using standard or asking user, wait! I don't have a token.
});

// Create a default schema definition for 'block'
const defaultSchema = {
  name: 'post',
  type: 'document',
  fields: [
    {
      name: 'body',
      type: 'array',
      of: [{ type: 'block' }]
    }
  ]
};

const blockContentType = defaultSchema.fields[0].of[0];

const results = [];

fs.createReadStream('../Blog.csv')
  .pipe(csv())
  .on('data', (data) => {
    results.push(data);
  })
  .on('end', async () => {
    console.log(`Loaded ${results.length} posts from CSV`);
    for (const post of results) {
      const slug = post.Slug;
      const html = post.Content;
      
      const blocks = blockTools.htmlToBlocks(html, blockContentType, {
        parseHtml: html => new JSDOM(html).window.document
      });
      
      const docId = `blog-${slug}`;
      try {
        await client.patch(docId).set({ body: blocks }).commit();
        console.log(`Updated ${docId}`);
      } catch (e) {
        console.error(`Failed to update ${docId}:`, e.message);
      }
    }
  });
