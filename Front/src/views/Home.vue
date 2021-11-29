<template>
  <div class="home">
    <app-mount
      :date="date"
      v-for="item in plain"
      :key="item.id"
      :metal="item.metal"
      :accs="item.accs"
      :dop="item.dop"
      :setting="item.setting"
      :armor="item.armor"
      :bil="item.bil"
      :mega="item.mega"
      :yota="item.yota"
      :tele="item.tele"
    />
  </div>
</template>

<script>
// @ is an alias to /src
import AppMount from "@/components/AppMount.vue";

export default {
  name: "Home",
  inject: ["date", "plain"],
  components: {
    AppMount,
  },
};
</script>
