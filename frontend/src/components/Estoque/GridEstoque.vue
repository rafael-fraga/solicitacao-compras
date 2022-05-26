<template>
  <div>
    <h1>Estoque</h1>

    <!--  Alertas da requisicao -->
    <v-alert v-if="loading == 'waiting'" prominent type="warning">
      Carregando dados do estoque...
    </v-alert>

    <v-alert v-else-if="loading == 'error'" prominent type="error">
      
        <a style="color: black"
          >Nao foi possivel carregar os dados do estoque.<br />Por gentileza,
          informe o setor de tecnologia
          <a style="color: blue" href="mailto:financeiro@brazas.com.br">clicando aqui</a>.</a>
    </v-alert>

    <v-alert v-else-if="loading == 'success'" prominent type="success">
      Dados do estoque carregados com sucesso.
    </v-alert>

    <!-- Data table -->

  <v-card>
    <v-card-title>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Procurar produto"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="produtos"
      :search="search"
      :loading="barra"
    ></v-data-table>
  </v-card>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      search: '',
      loading: 0,
      barra: true,
      headers: [
        {
          text: "Produto",
          align: "start",
          value: "produto",
        },
        { text: "Estoque atual", value: "estoqueatual" },
        { text: "Estoque minimo", value: "estoqueminimo" },
        { text: "Situacao", value: "situacao" },
      ],
      produtos: [],
      apiUrl: "https://628b088d667aea3a3e25f63a.mockapi.io/estoque",
    };
  },
  created: function() {
    this.requestEstoque();
  },
  methods: {
    requestEstoque(){
      this.loading = 'waiting';
      let apiResponse;

      fetch(this.apiUrl).then(async (response) => {
        apiResponse = await response.json();

        if (!response.ok) {
          this.loading = 'error';
          const error = (apiResponse && apiResponse.message) || response.statusText;
          return Promise.reject(error);
        }

        this.loading = 'success';

        this.produtos = apiResponse.map((produto) => {
          produto.estoqueatual > produto.estoqueminimo
            ? (produto.situacao = "ABAIXO do minimo")
            : (produto.situacao = "ACIMA do minimo");
          return produto;
        });

        if (this.loading !== 'error') {
          setTimeout(() => {
            this.loading = undefined;
          }, 4500);
        }
        this.barra = false;
      })
      .catch((error) => {
        this.loading = 'error';
        this.errorMessage = error;
        console.error("There was an error!", error);
        this.barra = false;
      });
    }
  }
};
</script>