<template>
  <div class="gsearch-input">
    <Filters :filters="search.filters" @removeFilter="removeFilter" />
    <div class="input-loader">
      <input
        id="search"
        class="rounded"
        v-model="search.query"
        placeholder="Search your library"
        type="text"
        @keyup.backspace="removeLastFilter"
      />
    </div>
  </div>
</template>

<script setup>
import Filters from "../Search/Filters.vue";
import Loader from "../shared/Loader.vue";
import useSearchStore from "../../stores/gsearch";

const search = useSearchStore();

function removeFilter(filter) {
  search.removeFilter(filter);
}

let counter = 0;

function removeLastFilter() {
  if (search.query === "") {
    counter++;

    if (counter > 0) {
      search.removeLastFilter();
    }
  } else {
    counter = 0;
  }
}
</script>

<style lang="scss">
.gsearch-input {
  padding: $small;
  display: flex;

  @include tablet-landscape {
    display: none;
  }

  .input-loader {
    width: 100%;
    border-radius: 0.4rem;
    position: relative;

    ._loader {
      position: absolute;
      top: -0.15rem;
      right: 2rem;
    }

    input {
      display: flex;
      align-items: center;
      width: 100%;
      border: none;
      line-height: 2.25rem;
      background-color: $black;
      color: inherit;
      font-size: 1rem;
      padding-left: 0.75rem;
      outline: 2px solid transparent;

      &:focus {
        outline: solid $accent;
      }
    }
  }
}
</style>
