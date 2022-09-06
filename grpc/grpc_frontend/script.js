import {greeterSetup} from ".\\greeter.js";
import {chatSetup} from ".\\chat.js";

window.onload = (event) => {
  greeterSetup();
  chatSetup();
};
