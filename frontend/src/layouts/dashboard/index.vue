<template>
  <div class="flex h-screen lg:overflow-hidden">
    <Sidebar />
    <div class="flex flex-col flex-1 w-full h-full">
      <Navigation />
      <slot />
    </div>
  </div>
</template>

<script src="./dashboard.js"></script>
