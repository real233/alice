<template>
  <div class="options border rounded">
    <div class="item info header">Filter by:</div>
    <div
      class="item"
      v-for="option in options"
      :key="option"
      @click="search.addFilter(option.icon)"
    >
      <div>
        <span class="icon">{{ option.icon }}</span>
        <span class="title">&nbsp;&nbsp;{{ option.title }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import useSearchStore from "../../stores/gsearch";

const search = useSearchStore();

const options = [
  {
    title: "Track",
    icon: "🎵",
  },
  {
    title: "Album",
    icon: "💿",
  },
  {
    title: "Artist",
    icon: "👤",
  },
  {
    title: "Playlist",
    icon: "🎧",
  },
  {
    title: "Folder",
    icon: "📁",
  },
];
</script>

<style lang="scss">
.right-search .options {
  display: flex;
  margin-bottom: $small;

  .item {
    margin: $small;
    width: 2.5rem;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    transition: all 0.2s ease-in-out;
    position: relative;
    background-color: $gray3;

    .title {
      position: absolute;
      left: 1.5rem;
      top: 0.5rem;
      visibility: hidden;
    }

    .icon {
      position: absolute;
      top: 0.5rem;
      left: 0.75rem;
    }

    &:hover {
      width: 5.5rem;
      background-color: $gray5;

      .title {
        visibility: visible;
      }
    }
  }

  .header {
    width: 5.5rem;
  }
}
</style>
