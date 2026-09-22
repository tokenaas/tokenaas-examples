# Contributing to TokenAAS Examples

Contributions should help a developer reach a first successful TokenAAS API call quickly. Prefer small, standalone examples over application-sized demos.

## Before you start

- Use [Discussions](https://github.com/tokenaas/tokenaas-examples/discussions) for integration questions.
- Open an example request before adding a large SDK or framework integration.
- Report platform vulnerabilities privately according to [SECURITY.md](SECURITY.md).
- Use `GET /v1/models` to confirm model IDs available to your API key.

## Example conventions

Each example should:

- read credentials from `TOKENAAS_API_KEY` and never hard-code a real key;
- default `TOKENAAS_BASE_URL` to `https://tokenaas.ai/v1` while allowing an override;
- allow the model ID to be overridden when a model is required;
- use an official SDK or direct HTTP with minimal dependencies;
- include a local README covering requirements, install, environment, run, expected output, and common errors;
- fail with a clear message when required environment variables are missing;
- avoid printing credentials, full authorization headers, or sensitive response data;
- write generated images and videos under `output/`, which is ignored by Git.

Do not add examples that make paid API calls during automated tests. CI performs syntax and secret-pattern checks only.

## Local checks

Run the checks relevant to your change from the repository root:

```bash
find curl -type f -name '*.sh' -print0 | xargs -0 -n1 bash -n
python3 -m compileall -q anthropic-sdk error-handling image-generation openai-sdk video-generation
node --check openai-sdk/node-chat/main.mjs
```

You may run the example manually with your own test key, but sanitize all output before adding it to an issue or pull request.

## Pull requests

Keep each pull request focused on one integration or one shared improvement. Explain the user goal, include exact verification commands, and update the root example table when adding a new directory.
