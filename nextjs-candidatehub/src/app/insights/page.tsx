import { client } from "@/sanity/client";
import Link from "next/link";
import Header from "@/components/Header";
import Footer from "@/components/Footer";

async function getInsights() {
  const query = `*[_type == "post" && slug.current != "to-delete"] | order(publishedAt desc) {
    _id,
    title,
    "slug": slug.current,
    publishedAt
  }`;
  const data = await client.fetch(query);
  return data;
}

export default async function InsightsPage() {
  const posts = await getInsights();

  return (
    <>
      <Header />
      <div className="section section-offwhite" style={{ minHeight: '100vh', paddingTop: '160px' }}>
        <div className="container">
          <div className="section-header text-center">
            <h1 className="section-title text-dark">Insights</h1>
            <p className="section-subtitle text-body">Latest thoughts on hiring, talent, and AI.</p>
          </div>
          <div className="markis-grid">
            {posts.map((post: any) => (
              <Link 
                key={post._id} 
                href={`/insights/${post.slug}`}
                className="glass-panel square-module"
                style={{ textDecoration: 'none', display: 'flex' }}
              >
                <div className="card-content">
                  <div className="card-text text-white">
                    <h3 style={{ fontSize: '1.25rem', marginBottom: '1rem', color: '#fff' }}>{post.title}</h3>
                    <time style={{ color: 'var(--text-secondary)', fontSize: '0.875rem' }}>
                      {new Date(post.publishedAt).toLocaleDateString("en-US", {
                        year: "numeric",
                        month: "long",
                        day: "numeric",
                      })}
                    </time>
                  </div>
                </div>
              </Link>
            ))}
          </div>
        </div>
      </div>
      <Footer />
    </>
  );
}
