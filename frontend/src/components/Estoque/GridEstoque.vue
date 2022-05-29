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
        label="Procurar (Codigo, Produto, Marca, Estoque, Situacao)"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="produtos"
      :search="search"
      :loading="barra"
    >
      <template v-slot:[`item.situacao`]="{ item }">
        <v-chip
        :color="getColor(item.situacao)"
        >
        {{ item.situacao }}
        </v-chip>
      </template>
    </v-data-table>
  </v-card>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      search: '',
      headers: [
        {
          text: "Codigo",
          align: "start",
          value: "codigo",
        },
        { text: "Produto", value: "nome"},
        { text: "Marca", value: "marca"},
        { text: "Estoque atual", value: "estoque" },
        { text: "Estoque minimo", value: "estoque_minimo" },
        { text: "Situacao", value: "situacao" },
      ],
    };
  },
  props: {
    produtos: Array,
    loading: String,
    barra: Boolean,
  },
  methods: {
    getColor (situacao){
      if(situacao == 'Abaixo do estoque'){
        return 'red';
      } else if (situacao == 'Neutro'){
        return 'grey';
      } else{
        return 'green';
      }
    },
  }
};
</script>