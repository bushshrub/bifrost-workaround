# bifrost-workaround

Bifrost decides which reasoning efforts a model accepts from its model-parameters datasheet. For a model that is not in the datasheet, it uses the model name, and only GPT-5.2+ and Grok models get `xhigh`. For other models, Bifrost changes `xhigh` to `high`. A self-hosted vLLM model that accepts only `low`/`medium`/`xhigh` then rejects the request.

This repo publishes a copy of the Bifrost datasheet with extra rows from `overrides.json`. A GitHub Action rebuilds it every 6 hours and publishes it to GitHub Pages. The JSON is not stored in the repo.

## Use

In the Bifrost UI, go to **Config → Model Settings → Model Parameters URL** and set:

```
https://bushshrub.github.io/bifrost-workaround/model-parameters.json
```

## Add a model

Add a row to `overrides.json`. The key is the model name without the provider prefix. `provider` must match the Bifrost provider.
