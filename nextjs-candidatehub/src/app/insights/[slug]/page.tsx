import { client } from "@/sanity/client";
import { PortableText } from "@portabletext/react";
import Link from "next/link";
import { notFound } from "next/navigation";
import Header from "@/components/Header";
import Footer from "@/components/Footer";

// Define the components for PortableText to match the brand styling
const portableTextComponents = {
  block: {
    h1: ({ children }: any) => <h1 style={{ fontSize: '2.5rem', fontWeight: 700, margin: '2rem 0 1rem', color: '#fff' }}>{children}</h1>,
    h2: ({ children }: any) => <h2 style={{ fontSize: '2rem', fontWeight: 700, margin: '2rem 0 1rem', color: '#fff' }}>{children}</h2>,
    h3: ({ children }: any) => <h3 style={{ fontSize: '1.5rem', fontWeight: 700, margin: '1.5rem 0 1rem', color: '#fff' }}>{children}</h3>,
    normal: ({ children }: any) => <p style={{ marginBottom: '1.5rem', fontSize: '1.125rem', color: 'rgba(255,255,255,0.8)', lineHeight: 1.7 }}>{children}</p>,
    blockquote: ({ children }: any) => <blockquote style={{ borderLeft: '4px solid var(--cta-orange)', paddingLeft: '1rem', fontStyle: 'italic', color: 'var(--text-secondary)', margin: '1.5rem 0' }}>{children}</blockquote>,
  },
  list: {
    bullet: ({ children }: any) => <ul style={{ paddingLeft: '1.5rem', marginBottom: '1.5rem', color: 'rgba(255,255,255,0.8)', listStyleType: 'disc', fontSize: '1.125rem' }}>{children}</ul>,
    number: ({ children }: any) => <ol style={{ paddingLeft: '1.5rem', marginBottom: '1.5rem', color: 'rgba(255,255,255,0.8)', listStyleType: 'decimal', fontSize: '1.125rem' }}>{children}</ol>,
  },
  marks: {
    link: ({ children, value }: any) => {
      const target = (value?.href || '').startsWith('http') ? '_blank' : undefined;
      return (
        <a href={value?.href} style={{ color: 'var(--cta-orange)', textDecoration: 'underline' }} target={target} rel={target === '_blank' ? 'noindex nofollow' : ''}>
          {children}
        </a>
      );
    },
  },
};

async function getPost(slug: string) {
  const query = `*[_type == "post" && slug.current == $slug][0] {
    title,
    publishedAt,
    body
  }`;
  const data = await client.fetch(query, { slug });
  return data;
}

export default async function InsightPostPage({ params }: { params: Promise<{ slug: string }> }) {
  const resolvedParams = await params;
  const post = await getPost(resolvedParams.slug);

  if (!post) {
    notFound();
  }

  return (
    <>
      <Header />
      <div style={{ minHeight: '100vh', paddingTop: '160px', paddingBottom: '100px', background: 'var(--bg-primary)' }}>
        <div className="container" style={{ maxWidth: '800px' }}>
          <Link href="/insights" style={{ color: 'var(--cta-orange)', textDecoration: 'none', marginBottom: '2rem', display: 'inline-block', fontWeight: 500 }}>
            &larr; Back to Insights
          </Link>
          <header style={{ marginBottom: '3rem', borderBottom: '1px solid var(--border-glass)', paddingBottom: '2rem' }}>
            <h1 style={{ fontSize: '3rem', fontWeight: 700, marginBottom: '1rem', color: '#fff', lineHeight: 1.2 }}>{post.title}</h1>
            <time style={{ color: 'var(--text-secondary)', fontSize: '1rem' }}>
              {new Date(post.publishedAt).toLocaleDateString("en-US", {
                year: "numeric",
                month: "long",
                day: "numeric",
              })}
            </time>
          </header>
          <div className="post-content">
            {post.body ? (
              <PortableText value={post.body} components={portableTextComponents} />
            ) : (
              // Fallback to local HTML export since Sanity body is empty
              <div 
                className="prose prose-invert max-w-none" 
                style={{ color: 'rgba(255,255,255,0.8)', fontSize: '1.125rem', lineHeight: 1.7 }}
                dangerouslySetInnerHTML={{ 
                  __html: require('@/data/blogs-html.json').find((b: any) => b.slug === resolvedParams.slug)?.html || '<p style="color: var(--text-secondary); font-style: italic;">This post has no content.</p>'
                }} 
              />
            )}
          </div>
        </div>
      </div>
      <Footer />
    </>
  );
}
