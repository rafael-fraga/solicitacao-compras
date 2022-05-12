<template>
  <div class="home">
    <div class="home__logo">
      <zd-image name="Zeedhi logo" src="../assets/zeedhi-logo.png"></zd-image>
      <img name="Zeedhi logo" src="../assets/zeedhi-logo.png"/>
      <h1> + </h1>
      <img alt="Vue logo" src="../assets/vue-logo.png">
    </div>
    <p class="home__title">Welcome to Your Zeedhi + Vue.js App</p>
    <p class="home__description">
      For a guide and recipes on how to configure or customize this
      <br>project, check out the <span class="zeedhi-style">Zeedhi</span> documentation below.
    </p>
    <div class="home__links">
      <a class="home__links__link" href="http://docs.zeedhi.com/" target="_blank">
        <v-icon>mdi-lightbulb-on</v-icon>
        <div><span class="zeedhi-style">Zeedhi</span> Docs</div>
      </a>
      <a class="home__links__link" href='https://docs.zeedhi.com/frontend/introduction' target="_blank">
        <v-icon>mdi-puzzle</v-icon>
        <div><span class="zeedhi-style">Zeedhi</span> Components</div>
      </a>
      <a class="home__links__link" href='https://vuejs.org' target="_blank">
        <v-icon>mdi-vuejs</v-icon>
        <div>Vue.js Docs</div>
      </a>
      <a class="home__links__link" href='https://materialdesignicons.com' target="_blank">
        <v-icon>mdi-drawing</v-icon>
        <div>MD Icons</div>
      </a>
      <a class="home__links__link" href='https://github.com/airbnb/javascript' target="_blank">
        <v-icon>mdi-code-tags-check</v-icon>
        <div>Airbnb Style Guide</div>
      </a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
};
</script>

<style lang="scss">
div.content {
  height: 100%;
  display: flex;

  .v-card__text {
    margin: auto;
  }
}

.home {
  padding: 16px;
  display: flex;
  flex-direction: column;
  text-align: center;
  line-height: normal;
  width: 100%;

  &__logo {
    display: flex;
    margin: 0 auto 43px;

    img {
      height: 77px;
      margin: auto;
      padding-right: 15px;
    }

    h1 {
      color: #e0e0e0;
      margin: auto 10px;
    }
  }

  &__title {
    font-weight: bold;
    font-size: 24px;
    color: #333333;
  }

  &__description {
    font-size: 14px;
    color: #828282;
    margin-bottom: 52px;
  }

  &__links {
    font-size: 14px;
    color: #4f4f4f;

    &__link {
      text-decoration: none;
      color: inherit;
      width: 80px;
      display: inline-block;
      vertical-align: text-top;
      margin: 0px 26px 26px;

      .v-icon {
        width: 48px;
        height: 48px;
        background: #e0e0e0;
        border-radius: 50%;
        margin-bottom: 16px;
      }
    }
  }

  .zeedhi-style {
    font-weight: 500;
    font-size: 14px;
    color: #4f4f4f;
  }
}
</style>
