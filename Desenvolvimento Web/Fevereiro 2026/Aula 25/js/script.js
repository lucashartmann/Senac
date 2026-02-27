let currentStepNum = 1;
const completedSteps = new Set();

function goToStep(step) {
    // Esconde todas as seções
    document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));

    // Mostra a seção atual
    document.getElementById(`step${step}`).classList.add('active');

    // Atualiza navegação
    document.querySelectorAll('.nav-btn').forEach((btn, index) => {
        btn.classList.remove('active');
        if (index + 1 === step) btn.classList.add('active');
    });

    // Atualiza indicadores
    currentStepNum = step;
    document.getElementById('currentStep').textContent = step;
    document.getElementById('stepIndicator').textContent = step;

    // Atualiza progresso
    const progress = (step / 15) * 100;
    document.getElementById('progressFill').style.width = `${progress}%`;

    // Scroll suave para o topo
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function markComplete(step) {
    completedSteps.add(step);
    document.querySelectorAll('.nav-btn')[step - 1].classList.add('completed');
}

function celebrateCompletion() {
    markComplete(15);
    alert('🎉 Parabéns! Você completou o curso de POO com JavaScript!\n\nAgora você domina:\n• Objetos e métodos\n• Prototypes\n• Classes ES6\n• Herança\n• e muito mais!');
}

// Códigos para cada etapa
const codes = {
    1: () => {
        const animal = {
            nome: "Bob",
            latir: function () {
                return "Au au";
            },
        };
        return [
            `animal.nome = "${animal.nome}"`,
            `animal.latir() = "${animal.latir()}"`
        ];
    },
    2: () => {
        const pessoa = {
            nome: "Roberto",
            getNome: function () {
                return this.nome;
            },
            setNome: function (novoNome) {
                this.nome = novoNome;
            },
        };
        const logs = [
            `pessoa.nome = "${pessoa.nome}"`,
            `pessoa.getNome() = "${pessoa.getNome()}"`
        ];
        pessoa.setNome("Roberto Alves");
        logs.push(`Após setNome("Roberto Alves"):`);
        logs.push(`pessoa.getNome() = "${pessoa.getNome()}"`);
        return logs;
    },
    3: () => {
        const text = "asd";
        const bool = true;
        const arr = [];
        return [
            `Prototype de "asd": String.prototype`,
            `Prototype de true: Boolean.prototype`,
            `arr.length = ${arr.length}`,
            `arr.prototype === Array.prototype: ${Object.getPrototypeOf(arr) === Array.prototype}`
        ];
    },
    4: () => {
        const myObject = { a: "b" };
        const mySecondObject = Object.create(myObject);
        return [
            `Prototype de myObject: Object.prototype`,
            `myObject.prototype === Object.prototype: ${Object.getPrototypeOf(myObject) === Object.prototype}`,
            `mySecondObject: { } (vazio, mas herda de myObject)`,
            `mySecondObject.prototype === myObject: ${Object.getPrototypeOf(mySecondObject) === myObject}`
        ];
    },
    5: () => {
        const cachorro = { raca: null };
        const pastorAlemao = Object.create(cachorro);
        pastorAlemao.raca = "Pastor Alemão";
        const bulldog = Object.create(cachorro);
        bulldog.raca = "Bulldog";
        return [
            `pastorAlemao.raca = "${pastorAlemao.raca}"`,
            `bulldog.raca = "${bulldog.raca}"`
        ];
    },
    6: () => {
        function criarCachorro(nome, raca) {
            const cachorro = Object.create({});
            cachorro.raca = raca;
            cachorro.nome = nome;
            return cachorro;
        }
        const bob = criarCachorro("Bob", "Vira lata");
        const jack = criarCachorro("Jack", "Poodle");
        return [
            `bob: { nome: "${bob.nome}", raca: "${bob.raca}" }`,
            `jack: { nome: "${jack.nome}", raca: "${jack.raca}" }`,
            `Prototype de jack: {} (objeto vazio)`
        ];
    },
    7: () => {
        function Cachorro(nome, raca) {
            this.nome = nome;
            this.raca = raca;
        }
        const husky = new Cachorro("Ozzy", "Husky");
        return [
            `husky: Cachorro { nome: "${husky.nome}", raca: "${husky.raca}" }`,
            `husky.nome = "${husky.nome}"`,
            `husky.raca = "${husky.raca}"`
        ];
    },
    8: () => {
        function Cachorro(nome, raca) {
            this.nome = nome;
            this.raca = raca;
        }
        const husky = new Cachorro("Ozzy", "Husky");
        Cachorro.prototype.uivar = function () {
            return "Auuu";
        };
        return [
            `Cachorro.prototype.uivar adicionado!`,
            `husky.uivar() = "${husky.uivar()}"`,
            `new Cachorro("Rex", "Pastor").uivar() = "Auuu"`
        ];
    },
    9: () => {
        class CachorroClasse {
            constructor(nome, raca) {
                this.nome = nome;
                this.raca = raca;
            }
        }
        const jeff = new CachorroClasse("Jeff", "Labrador");
        return [
            `jeff: CachorroClasse { nome: "${jeff.nome}", raca: "${jeff.raca}" }`,
            `Prototype: CachorroClasse.prototype`
        ];
    },
    10: () => {
        class Caminhao {
            constructor(eixos, cor) {
                this.eixos = eixos;
                this.cor = cor;
            }
            descreverCaminhao() {
                return `Este caminhão tem ${this.eixos} eixos e é da cor ${this.cor}.`;
            }
        }
        const scania = new Caminhao(6, "Vermelha");
        Caminhao.motor = 4.0;
        const c2 = new Caminhao(4, "Preta");
        Caminhao.prototype.motor = 4.0;
        const c3 = new Caminhao(6, "Azul");
        return [
            `scania.descreverCaminhao():`,
            `"${scania.descreverCaminhao()}"`,
            `c2.motor (estático): undefined`,
            `c3.motor (prototype): ${c3.motor}`
        ];
    },
    11: () => {
        class Humano {
            constructor(nome, idade) {
                this.nome = nome;
                this.idade = idade;
            }
        }
        const roberto = new Humano("Roberto", 31);
        Humano.prototype.idade = "Não definida";
        const joao = new Humano("João");
        return [
            `roberto: Humano { nome: "${roberto.nome}", idade: ${roberto.idade} }`,
            `roberto.idade = ${roberto.idade}`,
            `joao.idade = "${joao.idade}" (do prototype)`,
            `roberto.idade ainda = ${roberto.idade} (próprio valor)`
        ];
    },
    12: () => {
        class Aviao {
            constructor(marca, turbinas) {
                this.marca = marca;
                this.turbinas = turbinas;
            }
        }
        const asas = Symbol();
        Aviao.prototype[asas] = 2;
        const boeing = new Aviao("Boeing", 10);
        return [
            `boeing: Aviao { marca: "${boeing.marca}", turbinas: ${boeing.turbinas} }`,
            `boeing[asas] = ${boeing[asas]}`,
            `Aviao.prototype[asas] = ${Aviao.prototype[asas]}`
        ];
    },
    13: () => {
        class Post {
            constructor(titulo, descricao, tags) {
                this.titulo = titulo;
                this.descricao = descricao;
                this.tags = tags;
            }
            get exibirTitulo() {
                return `Você está lendo: ${this.titulo}`;
            }
            set adicionarTags(tags) {
                const tagsArray = tags.split(", ");
                this.tags = tagsArray;
            }
        }
        const myPost = new Post("Algum post", "É um post sobre programação");
        const titulo = myPost.exibirTitulo;
        myPost.adicionarTags = "programacao, javascript, js";
        return [
            `myPost.exibirTitulo:`,
            `"${titulo}"`,
            `myPost.tags após adicionar:`,
            `[${myPost.tags.map(t => `"${t}"`).join(", ")}]`
        ];
    },
    14: () => {
        class Mamifero {
            constructor(patas) {
                this.patas = patas;
            }
        }
        class Lobo extends Mamifero {
            constructor(patas, nome) {
                super(patas);
                this.nome = nome;
            }
            uivar() {
                return "Auuuu!";
            }
        }
        const shark = new Lobo(4, "Shark");
        return [
            `shark: Lobo { patas: ${shark.patas}, nome: "${shark.nome}" }`,
            `shark.patas (herdado de Mamifero) = ${shark.patas}`,
            `shark.nome (próprio) = "${shark.nome}"`,
            `shark.uivar() = "${shark.uivar()}"`
        ];
    },
    15: () => {
        class Mamifero {
            constructor(patas) {
                this.patas = patas;
            }
        }
        class Lobo extends Mamifero {
            constructor(patas, nome) {
                super(patas);
                this.nome = nome;
            }
        }
        class Cachorro { }
        class Post { }
        const shark = new Lobo(4, "Shark");
        return [
            `shark instanceof Lobo: ${shark instanceof Lobo}`,
            `Lobo instanceof Mamifero: ${Lobo instanceof Mamifero}`,
            `new Lobo() instanceof Mamifero: ${new Lobo(4, "teste") instanceof Mamifero}`,
            `new Post() instanceof Cachorro: ${new Post("a", "b") instanceof Cachorro}`
        ];
    }
};

function runCode(step) {
    const consoleEl = document.getElementById(`console${step}`);
    consoleEl.innerHTML = '<div class="console-line"><span class="console-prompt">$</span><span class="console-input">node scripts.js</span></div>';

    const outputs = codes[step]();
    outputs.forEach(output => {
        const line = document.createElement('div');
        line.className = 'console-line';
        line.innerHTML = `<span class="console-output">${output}</span>`;
        consoleEl.appendChild(line);
    });

    // Adiciona linha final
    const endLine = document.createElement('div');
    endLine.className = 'console-line';
    endLine.innerHTML = '<span class="console-prompt">$</span><span class="console-input" style="animation: blink 1s infinite;">_</span>';
    consoleEl.appendChild(endLine);
}

// Navegação por teclado
document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' && currentStepNum < 15) {
        goToStep(currentStepNum + 1);
    } else if (e.key === 'ArrowLeft' && currentStepNum > 1) {
        goToStep(currentStepNum - 1);
    }