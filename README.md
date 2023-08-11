# rebelai

> free access to multiple proprietary ai models in python

# mission

exploit freely available apis to gain access to ai models because
proprietary ai companies took advantage of our open source
resources to develop their proprietary money machines unfairly

( fuck you """""""""""""""""""""""""""""open"""""""""""""""""""""""""""""ai )

# installation

```sh
$ pip install rebelai
```

# usage

module structure :

-   `rebelai` -- top level package
    -   `const` -- all constants, defaults, etc
    -   `enums` -- all enums for convenience sake
        -   `ProdiaModel` -- enum for prodia image generation ai models
        -   `ProdiaSampler` -- enum for prodia image generation samplers
        -   `DeepAIModel` -- enum for deepai models
    -   `ai` -- all ai wrappers
        -   `alpaca` -- access to alpaca models
            -   `alpaca_7b` -- the 7 billion neuron alpaca model
        -   `deepai` -- access to all deepai models
            -   `deepai` -- generic function for deepai access for free, takes DeepAIModel, see doc string for more info
        -   `gpt` -- access to "open"ai models ( kinda )
            -   `gpt3` -- access to gpt3 model
            -   `gpt4` -- access to gpt3 model ( youchat )
        -   `pollinations` -- access to pollinations image generation api
            -   `pollinations` -- access to the generation model
        -   `prodia` -- access to prodia image generation api ( limited access and proxies dont seem to work :( )
            -   `prodia` -- generic function to access prodia api, takes `ProdiaModel` and `ProdiaSampler`, see doc string
        -   `inferkit` -- access inferkit text completion model
            -   `standard` -- standard model access
        -   `deepl` -- access to deepl translation
            -   `deepl` -- generic deepl function, see doctring for help

# tips

-   use proxies ( for example gimmeproxy api,, https://gimmeproxy.com/api/getProxy?post=true&get=true&user-agent=true&supportsHttps=true&protocol=http&minSpeed=20&curl=true )
    -   dont forget to test if theyre responsive by making a proxies request to for example https://example.com/
-   check docstrings, they have info about arguments and proxies
