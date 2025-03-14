import SwaggerParser from '@apidevtools/swagger-parser';
import type { OpenAPIObject } from 'openapi3-ts';
import { resolveConfig } from 'prettier';
import { generateZodClientFromOpenAPI, getZodSchema } from 'openapi-zod-client';
import axios from 'axios';
import path from 'path';

async function generateZodiosClient() {
    const specUrl = 'https://api.compasslabs.ai/openapi.json';
    const openApiDoc = (await SwaggerParser.parse(
        await axios.get(specUrl).then((res) => res.data)
    )) as OpenAPIObject;
    const prettierConfig = await resolveConfig('./');
    const result = await generateZodClientFromOpenAPI({
        openApiDoc,
        distPath: path.join(__dirname, '../src/client.ts'),
        prettierConfig,
        options: { withDescription: true },
    });
    console.log(result);
}

async function main() {
    await generateZodiosClient();
}

main().catch(console.error);
