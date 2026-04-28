const { createClient } = require('@sanity/client');
const fs = require('fs');
const csv = require('csv-parser');

const client = createClient({
  projectId: 'p65whnge',
  dataset: 'production',
  useCdn: false,
  apiVersion: '2023-05-03',
  token: process.env.SANITY_API_TOKEN
});

const results = [];

fs.createReadStream('../Blog.csv')
  .pipe(csv())
  .on('data', (data) => {
    results.push(data);
  })
  .on('end', async () => {
    console.log(`Loaded ${results.length} posts from CSV`);
    for (const post of results) {
      const slug = post.Slug.replace(/["]/g, ""); // Clean the slug from quotes if any
      const html = post.Content;
      
      const docId = `blog-${slug}`;
      try {
        await client.patch(docId).set({ htmlBody: html }).commit();
        console.log(`Updated ${docId} with HTML content`);
      } catch (e) {
        console.error(`Failed to update ${docId}:`, e.message);
      }
    }
  });
