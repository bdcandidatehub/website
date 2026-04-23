import { client } from "@/sanity/client";
import AnimatedPage from "@/components/AnimatedPage";

// Fetch data on the server side
async function getHomepageData() {
  const query = `*[_type == "homepage"][0] {
    heroHeadline,
    heroSubtext,
    ctaText,
    markisCards,
    outcomes
  }`;
  
  const data = await client.fetch(query);
  return data || {};
}

export default async function Page() {
  const data = await getHomepageData();
  
  return <AnimatedPage data={data} />;
}
