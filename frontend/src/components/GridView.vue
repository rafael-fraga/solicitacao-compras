<template>
  <div>
    <v-alert v-if="carregando == 0" shaped prominent type="warning">
      <strong></strong>Carregando dados do estoque...<strong></strong>
    </v-alert>
    <v-alert v-else-if="carregando == 1" shaped prominent type="error">
      <strong><a style="color:black;">Nao foi possivel carregar os dados do estoque por problemas tecnicos internos.<br>Por gentileza, informe o setor de tecnologia <a style="color:blue" href="mailto:test@test.com">clicando aqui</a>.</a></strong>
    </v-alert>
    <v-alert v-else-if="carregando == 2" shaped prominent type="success">
      <strong>Dados do estoque carregados com sucesso.</strong>
    </v-alert>
    <v-data-table
      :headers="headers"
      :items="produtos"
      :items-per-page="5"
      class="elevation-1"
    ></v-data-table>
    <p>{{ totalVuePackages }}</p>
  </div>
</template>

<script>
export default {
  name: "first-grid",
  // mounted () {
  //   alert('test');
  //   this.data
  // },
  // methods () {

  // },

  created() {
    this.carregando = 0;
    // GET request using fetch with error handling
    let data;
    fetch("https://628b088d667aea3a3e25f63a.mockapi.io/estoque")
      .then(async (response) => {
        data = await response.json();
        if (!response.ok) {
          this.carregando = 1;
          // get error message from body or default to response statusText
          const error = (data && data.message) || response.statusText;
          return Promise.reject(error);
        }
        this.tratarDados(data);
        this.carregando = 2;
        this.totalVuePackages = data.total;
        setTimeout(() => { this.carregando = 4}, 5000);

      })
      .catch((error) => {
        this.errorMessage = error;
        console.error("There was an error!", error);
      });
  },
  methods: {
    tratarDados (data) {
      console.log(data);
    }

  },
  data() {
    return {
      totalVuePackages: "nada",
      carregando: 0,
      dados: [],
      headers: [
        {
          text: "Produto",
          align: "start",
          value: "produto",
        },
        { text: "Estoque atual", value: "estoqueAtual" },
        { text: "Estoque minimo", value: "estoqueMinimo" },
        { text: "Situacao", value: "situacao" },
      ],
      produtos: this.dados,
    };
  },
};
</script>
