<template>
  <div>
    <v-card
      style="
        margin: 0px 10px 10px 10px;
        border-radius: 10px;
        min-height: 400px;
        padding: 20px 20px 0px 20px;
      "
    >
      <h1 style="padding-bottom: 15px">Ranking</h1>
      <section>
        <v-autocomplete
          v-model="slugSelected"
          label="Produto"
          auto-select-first
          clearable
          dense
          :items="slug"
          v-on:change="procurarFornecedor"
        ></v-autocomplete>
      </section>
      <section style="padding-top: 30px">
        <v-data-table
          :headers="topo"
          :items="produtinhos"
          :options="{ page: 1, itemsPerPage: 5 }"
          :sort-by="['cotacao']"
          :sort-desc="[true]"
        >
          <template v-slot:[`item.disponivel`]="{ item }">
            <v-simple-checkbox
              :ripple="false"
              v-model="item.disponivel"
            ></v-simple-checkbox>
          </template>
          <template v-slot:[`item.cotacao`]="props">
            <v-edit-dialog
              :return-value.sync="props.item.cotacao"
              large
              persistent
              @save="save"
              @cancel="cancel"
              @close="close"
            >
              <v-chip
                v-if="props.item.cotacao === 0"
                color="yellow"
                label
                large
              >
                Adicionar uma cotação
              </v-chip>
              <div v-else>
                R$ {{ props.item.cotacao }} / {{ props.item.unidade }}
              </div>
              <template v-slot:input>
                <div class="mt-4 text-h6">Atualizar cotação (R$)</div>
                <v-text-field
                  v-model="props.item.cotacao"
                  label="R$"
                  single-line
                  counter
                  autofocus
                ></v-text-field>
              </template>
            </v-edit-dialog>
          </template>
        </v-data-table>
        <v-btn color="success" @click="adicionarProduto" style="float: right">
          Adicionar produto(s)
        </v-btn>
        <v-snackbar
          elevation="18"
          v-model="snack"
          :timeout="3000"
          :color="snackColor"
          large
        >
          {{ snackText }}

          <template v-slot:action="{ attrs }">
            <v-btn v-bind="attrs" text @click="snack = false"> Fechar </v-btn>
          </template>
        </v-snackbar>
      </section>
    </v-card>

    <v-card
      style="
        margin: 0px 10px 10px 10px;
        border-radius: 10px;
        min-height: 400px;
        padding: 20px 20px 0px 20px;
      "
    >
      <h1 style="padding-bottom: 15px">Solicitação de compra</h1>
      <section style="padding-top: 30px">
        <v-data-table
          :headers="relatorioHeader"
          :items="desserts"
          :options="{ page: 1, itemsPerPage: 5 }"
          :sort-by="['cotacao']"
          :sort-desc="[true]"
        >
        <template v-slot:[`item.cotacao`]="props">
          <div>R$ {{ props.item.cotacao }}</div>
        </template>
          <template v-slot:[`item.quantidade`]="props">
            <v-edit-dialog
              :return-value.sync="props.item.quantidade"
              large
              persistent
              @save="saveQuantidade(props.item)"
              @cancel="cancel"
              @close="close"
            >
              <v-chip
                v-if="props.item.quantidade === 0"
                color="yellow"
                label
                large
              >
                Adicionar quantidade
              </v-chip>
              <div v-else>
                {{ props.item.quantidade }}
              </div>
              <template v-slot:input>
                <div class="mt-4 text-h6">
                  Atualizar quantidade <br />(Use vírgula para números decímais)
                </div>
                <v-text-field
                  v-model="props.item.quantidade"
                  single-line
                  counter
                  autofocus
                ></v-text-field>
              </template>
            </v-edit-dialog>
          </template>
        </v-data-table>
        <v-btn color="success" @click="enviarSolicitacao" style="float: right">
          Enviar solicitação de compra
        </v-btn>
      </section>
    </v-card>
  </div>
</template>

<script>
export default {
  data: () => ({
    snack: false,
    snackColor: "",
    snackText: "",
    pagination: {},
    numberValue: 0,
    headers: [
      {
        text: "Código",
        align: "start",
        value: "codigo",
      },
      { text: "Produto", value: "nome" },
      { text: "Marca", value: "marca" },
      { text: "Selecionar", value: "disponivel" },
    ],
    desserts: [],
    slugSelected: "",
    search: "",
    produtinhos: [],
    topo: [
      { text: "Produto", align: "start", value: "nome" },
      { text: "Código", value: "codigo" },
      { text: "Marca", value: "marca" },
      { text: "Cotacao", value: "cotacao" },
      { text: "Selecionar", value: "disponivel", sortable: false },
    ],
    relatorioHeader: [
      {
        text: "Código",
        align: "start",
        value: "codigo",
      },
      { text: "Produto", value: "nome" },
      { text: "Marca", value: "marca" },
      { text: "Cotação", value: "cotacao" },
      { text: "Quantidade", value: "quantidade" },
      { text: "Valor final", value: "valorfinal" },
    ],
  }),
  props: {
    produtos: Array,
    slug: Array,
    fornecedores: Array,
  },
  methods: {
    enviarSolicitacao(){
      this.desserts.forEach((item) => {
        item.valorfinal = item.valorfinal.split(' ')[1]
      })

    fetch('Sua rota POST aqui', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(this.desserts),
    })
    .then(response => response.json())
    .then(data => {
      console.log('Tudo ok:', data);
    })
    .catch((error) => {
      console.error('Erro:', error);
    });
    },
    tratarMoeda(valor){
      if(valor.includes(',')){
        valor = valor.replace(',', '.');
      }
      return parseFloat(valor);
    },
    saveQuantidade(produto){
      produto.valorfinal = `R$ ${ produto.cotacao * this.tratarMoeda(produto.quantidade)}`;
    },
    procurarFornecedor() {
      const filtrados = this.produtos.filter(
        (produto) => produto.slug == this.slugSelected
      );
      this.produtinhos = filtrados;
    },
    adicionarProduto() {
      const adicionar = this.produtinhos.filter(
        (produto) => produto.disponivel == true
      );
      adicionar.forEach((item) => {
        if (!this.desserts.includes(item)) {
          if (item.cotacao == 0) {
            this.snack = true;
            this.snackColor = "error";
            this.snackText = "Adicione uma cotação ao produto selecionado.";
          } else {
            this.desserts.unshift(item);
            this.snack = true;
            this.snackColor = "success";
            this.snackText = `O produto "${item.nome}" foi adicionado com sucesso!`;
          }
        } else {
          this.snack = true;
          this.snackColor = "error";
          this.snackText = "Este produto já existe na solicitação!";
        }
        this.limparSelects();
      });
    },
    limparSelects() {
      this.produtinhos.forEach((produto) => {
        produto.disponivel = false;
      });
    },
    deleteItem(item) {
      this.desserts = this.desserts.filter((produto) => produto != item);
    },
    save() {
      this.snack = true;
      this.snackColor = "success";
      this.snackText = "Cotação salva!";
    },
    cancel() {
      this.snack = true;
      this.snackColor = "error";
      this.snackText = "Cancelado";
    },
    close() {
      console.log("Alerta fechado!");
    },
  },
};
</script>
