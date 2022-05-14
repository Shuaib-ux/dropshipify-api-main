<template>
  <component :is="layout">
    <Loader />
    <slot />
  </component>
</template>

<script src="./base.js"></script>
