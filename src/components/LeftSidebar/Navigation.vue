<template>
  <div class="side-nav-container" :class="{ collapsed: props.collapsed }">
    <router-link
      v-for="menu in menus"
      :key="menu.name"
      :to="{ name: menu.route_name, params: menu.params }"
    >
      <div class="nav-button" id="home-button">
        <div class="in">
          <div class="nav-icon image" :id="`${menu.name}-icon`"></div>
          <span>{{ menu.name }}</span>
        </div>
      </div>
    </router-link>
  </div>
</template>

<script setup>
const menus = [
  {
    name: "home",
    route_name: "Home",
  },
  {
    name: "albums",
    route_name: "AlbumsView",
  },
  {
    name: "artists",
    route_name: "ArtistsView",
  },
  {
    name: "playlists",
    route_name: "Playlists",
  },
  {
    name: "folders",
    route_name: "FolderView",
    params: { path: "$home" },
  },
  {
    name: "tags",
  },
  {
    name: "settings",
    route_name: "SettingsView",
  },
];

const props = defineProps({
  collapsed: {
    type: Boolean,
    default: false,
  },
});
</script>

<style lang="scss">
.collapsed {
  .nav-button {
    margin-top: 5px;

    span {
      display: none;
    }

    .in {
      width: 100%;
      flex-direction: column;
    }
  }
}

.side-nav-container {
  color: #fff;
  margin-bottom: 1rem;
  padding: 10px $small $small;
  margin-top: 1rem;
  text-transform: capitalize;

  .nav-button {
    border-radius: $small;
    display: flex;
    align-items: flex-start;
    justify-content: flex-start;
    height: 100%;
    padding: 0.6rem 0 0.6rem 0;

    &:hover {
      background-color: $gray;
    }

    .nav-icon {
      height: 2rem;
      width: 2rem;
      margin: 0 $small 0 $small;
      border-radius: $small;
      background-color: rgb(26, 24, 24);
    }

    .in {
      display: flex;
      align-items: center;

      & > * {
        background-size: 1.5rem;
      }
    }

    #home-icon {
      background-image: url(../../assets/icons/home.svg);
    }

    #albums-icon {
      background-image: url(../../assets/icons/album.svg);
    }

    #artists-icon {
      background-image: url(../../assets/icons/artist.svg);
    }

    #playlists-icon {
      background-image: url(../../assets/icons/playlist.svg);
    }

    #mixes-icon {
      background-image: url(../../assets/icons/mix.svg);
    }

    #folders-icon {
      background-image: url(../../assets/icons/folder.svg);
    }
    #settings-icon {
      background-image: url(../../assets/icons/settings.svg);
    }
    #tags-icon {
      background-image: url(../../assets/icons/tag.svg);
    }
  }
}
</style>
