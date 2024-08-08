<template>
  <link href="https://fonts.googleapis.com/css?family=Bowlby One SC" rel="stylesheet" />
  <header class="">
    <span class="animelist-text link">animelist</span>
    <span class="logo">AO</span>
    <span class="witelist-text link">waitlist</span>
  </header>
</template>

<style>
.logo {
  font-family: 'Bowlby One SC';
  font-size: 50px;
  color: #049548;
}

header {
  background-color: rgba(206, 255, 208, 0.4);
  display: flex;
  justify-content: center;
  align-items: center;
  column-gap: 15px;
  margin-bottom: 37px;
}
header span {
  cursor: pointer;
}
header .link:hover {
  color: #049548;
  transition: all 0.2s linear;
}
</style>
