import SwaggerParser from '@apidevtools/swagger-parser';
import type { OpenAPIObject } from 'openapi3-ts';
import { resolveConfig } from 'prettier';
import { generateZodClientFromOpenAPI, getZodSchema } from 'openapi-zod-client';
import axios from 'axios';
import path from 'path';
import fs from "fs";

const GENERATED_CLIENT_PATH = path.join(__dirname, "../src/client.ts")


async function generateZodiosClient() {
  const specUrl = 'https://api.compasslabs.ai/openapi.json';
  const openApiDoc = (await SwaggerParser.parse(
    await axios.get(specUrl).then((res) => res.data)
  )) as OpenAPIObject;
  const prettierConfig = await resolveConfig('./');
  const result = await generateZodClientFromOpenAPI({
    openApiDoc,
    distPath: GENERATED_CLIENT_PATH,
    prettierConfig,
    options: { withDescription: true },
  });
  injectCompassOriginHeader()
  console.log("Generated client");
}


function injectCompassOriginHeader() {
  let clientCode = fs.readFileSync(GENERATED_CLIENT_PATH, "utf-8");

  const updatedFunction = `
export function createApiClient(baseUrl: string, options?: ZodiosOptions) {
  const defaultHeaders = {
    "x-compass-origin": "ts-sdk",
  };

  const finalOptions: ZodiosOptions = {
    ...options,
    axiosConfig: {
      ...options?.axiosConfig,
      headers: {
        ...defaultHeaders,
        ...options?.axiosConfig?.headers,
      },
    },
  };

  return new Zodios(baseUrl, endpoints, finalOptions);
}
`;

  clientCode = clientCode.replace(
    /export function createApiClient\([^)]*\)\s*\{[\s\S]*?\}/,
    updatedFunction.trim()
  );

  fs.writeFileSync(GENERATED_CLIENT_PATH, clientCode, "utf-8");

  console.log("Header injector injected into client");
}


async function main() {
  await generateZodiosClient();
}

main().catch(console.error);
