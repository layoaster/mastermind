# Mastermind API
A simple REST API for the original
[MasterMind](https://en.wikipedia.org/wiki/Mastermind_(board_game))
game.


## Requirements:
1. [Docker](https://www.docker.com/)
2. [Docker Compose](https://docs.docker.com/compose/)
3. [Node.JS](https://nodejs.org/) (only for API docs generation)


## Installation & usage

1. Build the docker image.

```bash
docker-compose build mastermind
```

2. Run the container (detached)

```bash
docker-compose up -d mastermind
```

When running in detached mode you can get the container output with:

```bash
docker-compose logs -f mastermind
```

## API reference

The API documentation is located in the `docs/api/` folder.

To generate the documentation install the `raml2html` package:

```bash
npm i -g raml2html
```

so documentation can be generated it with:

```bash
raml2html api.raml > index.html
```

**Notes**

Due to a [bug](https://github.com/raml2html/raml2html/issues/328) with
`raml2html` every property with an array of enums is not properly
rendered so please take into account the following:

* The length of code pegs is `4`.
* The are six code pegs colors available: `blue`, `yellow`, `red`
`green` and `purple`.
* The key pegs are `white` and `black`.
