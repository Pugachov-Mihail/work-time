<template>
  <router-view />
  <div id="nav">
    <router-link to="/">Планы</router-link> |
    <router-link to="/fact">Внести факт</router-link>
  </div>
</template>

<script>
export default {
  name: "App",
  provide() {
    return {
      date: new Date().toLocaleDateString(),
      plain: [
        {
          metal: "0",
          accs: "0",
          dop: "0",
          setting: "0",
          armor: "0",
          bil: "0",
          mega: "0",
          yota: "0",
          tele: "0",
        },
      ],
    };
  },

  data() {
    return {
      date: new Date().toLocaleDateString(),
      name: "Заполнить план на месяц",
    };
  },
};
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #02162b;
}
body {
  background-color: rgb(219, 239, 255);
}

#nav {
  padding: 30px;
  text-align: left;
}

#nav a {
  font-weight: bold;
  color: #16944b;
}

#nav a.router-link-exact-active {
  color: #00177c;
}
</style>
