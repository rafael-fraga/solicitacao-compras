<template>
  <div>
    <div>
      <h1 style="padding-bottom: 20px">Ranking</h1>
      <section>
        <v-row>
          <v-col>
            <v-autocomplete
              v-model="slugSelected"
              label="Produto"
              auto-select-first
              clearable
              dense
              :items="slug"
              v-on:change="procurarFornecedor"
            ></v-autocomplete>
          </v-col>
          <!-- <v-col>
        <v-autocomplete
          v-model="fornecedoresSelected"
          auto-select-first
          clearable
          dense
          :items="fornecedores"
        ></v-autocomplete>
      </v-col> -->
          <v-col> </v-col>
        </v-row>
      </section>

      <section>
        <div>
          <v-data-table
            :headers="topo"
            :items="produtinhos"
            class="elevation-1"
            hide-default-footer
          >
            <template v-slot:[`item.disponivel`]="{ item }">
              <v-simple-checkbox
                :ripple="false"
                v-model="item.disponivel"
              ></v-simple-checkbox>
            </template>
          </v-data-table>
          <v-row style="float: right; padding-top: 10px">
            <v-col>
              <v-btn color="success" dark @click="adicionarProduto">
                Adicionar produto(s)
              </v-btn>
            </v-col>
          </v-row>
        </div>
      </section>
    </div>
    <div style="padding-bottom: 20px; padding-top: 20px" />
    <h1> Solicitacao final </h1>
    <div>
<template>
  <v-simple-table>
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">
            Name
          </th>
          <th class="text-left">
            Calories
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="item in desserts"
          :key="item.nome"
        >
          <td>{{ item.codigo }}</td>
          <td>{{ item.nome }}</td>
          <td><v-text-field
          v-model="item.preco"
          label="Amount"
          value="10.00"
          prefix="$"
          dense
        ></v-text-field></td>
        <v-icon
          @click="deleteItem(item)"
          color="red"
        >
          mdi-delete
        </v-icon>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
</template>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    numberValue: 0,
    headers: [
      {
        text: "Codigo",
        align: "start",
        value: "codigo",
      },
      { text: "Produto", value: "nome" },
      { text: "Marca", value: "marca" },
      { text: "Selecionar", value: "disponivel" },
    ],
    desserts: [],
    slugSelected: "",
    fornecedoresSelected: "",
    search: "",
    produtinhos: [],
    relatorio: [],
    topo: [
      {
        text: "Codigo",
        align: "start",
        value: "codigo",
      },
      { text: "Produto", value: "nome" },
      { text: "Marca", value: "marca" },
      { text: "Selecionar", value: "disponivel" },
    ],
  }),
  props: {
    produtos: Array,
    slug: Array,
    fornecedores: Array,
  },
  methods: {
    procurarFornecedor() {
      const filtrados = this.produtos.filter(
        (produto) => produto.slug == this.slugSelected
      );
      this.produtinhos = filtrados;
    },
    adicionarProduto() {
      const relatoorio = this.produtinhos.filter(
        (produto) => produto.disponivel == true
      );
      relatoorio.forEach((item) => { this.desserts.unshift(item)});
    },
    deleteItem(item) {
      this.desserts = this.desserts.filter((produto) => produto != item);
    }
  },
};
</script>
