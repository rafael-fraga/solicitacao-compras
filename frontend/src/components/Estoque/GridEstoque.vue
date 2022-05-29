<template>
  <div>
      <v-img
        alt="Logo Brazas"
        src="https://brazas.com.br/bh/wp-content/uploads/sites/3/2021/04/brazas_branco_slogan.png"
        max-width="300"
      />
    <v-card style="margin: 10px 10px 10px 10px; border-radius: 10px">
          <!--  Alertas da requisicao -->
      <v-alert dark v-if="loading == 'waiting'" prominent type="warning">
        Carregando dados do estoque...
      </v-alert>

      <v-alert v-else-if="loading == 'error'" prominent type="error">
        <a style="color: black"
          >Nao foi possivel carregar os dados do estoque.<br />Por gentileza,
          informe o setor de tecnologia
          <a style="color: blue" href="mailto:financeiro@brazas.com.br"
            >clicando aqui</a
          >.</a
        >
      </v-alert>

      <v-alert v-else-if="loading == 'success'" prominent type="success">
        Dados do estoque carregados com sucesso.
      </v-alert>
      <h1 style="padding: 20px 20px 0px 20px;">Estoque</h1>
      <!-- Data table -->
      <v-card>
        <v-card-title>
          <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Procurar por: Código, Produto, Marca, Estoque ou Situação"
            single-line
            hide-details
          ></v-text-field>
        </v-card-title>
        <v-data-table
          :headers="headers"
          :items="produtos"
          :search="search"
          :loading="barra"
          :options="{page: 1, itemsPerPage: 5}"
          :mobile=true
          style="font-family: Roboto, Arial, sans-serif;"
        >
          <template v-slot:[`item.situacao`]="{ item }">
            <v-chip :color="getColor(item.situacao)" label>
              <b><span>{{ item.situacao }}</span></b>
            </v-chip>
          </template>
        </v-data-table>
      </v-card>
    </v-card>
  </div>
</template>
<style scoped>
</style>
<script>
export default {
  data: function () {
    return {
      search: "",
      headers: [
        {
          text: "Código",
          align: "start",
          value: "codigo",
        },
        { text: "Produto", value: "nome" },
        { text: "Marca", value: "marca" },
        { text: "Estoque atual", value: "estoque" },
        { text: "Estoque mínimo", value: "estoque_minimo" },
        { text: "Situação", value: "situacao" },
      ],
    };
  },
  props: {
    produtos: Array,
    loading: String,
    barra: Boolean,
  },
  methods: {
    getColor(situacao) {
      if (situacao == "Abaixo do estoque.⠀⠀⠀⠀⠀⠀⠀⠀⠀") {
        return "red";
      } else if (situacao == "Estoque mínimo não cadastrado.") {
        return "grey";
      } else {
        return "green";
      }
    },
  },
};
</script>
<style>
</style>