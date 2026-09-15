import OpenAI from "openai";

const apiKey = process.env.TOKENAAS_API_KEY;
if (!apiKey) {
  console.error("Set TOKENAAS_API_KEY first.");
  process.exit(1);
}

const client = new OpenAI({
  apiKey,
  baseURL: process.env.TOKENAAS_BASE_URL || "https://tokenaas.ai/v1",
  timeout: 60_000,
  maxRetries: 2,
});

const model = process.env.TOKENAAS_TEXT_MODEL || "deepseek-v4-flash";

const response = await client.chat.completions.create({
  model,
  messages: [{ role: "user", content: "Explain large language models in three sentences." }],
});

console.log(response.choices[0].message.content);
