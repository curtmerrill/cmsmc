/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ 572:
/***/ ((__unused_webpack___webpack_module__, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   Framer: () => (/* binding */ e),
/* harmony export */   autoInitFrames: () => (/* binding */ a),
/* harmony export */   initFrame: () => (/* binding */ d),
/* harmony export */   initFrameAndPoll: () => (/* binding */ m),
/* harmony export */   observeIframe: () => (/* binding */ n),
/* harmony export */   sendFrameHeight: () => (/* binding */ r),
/* harmony export */   sendHeightOnFramerInit: () => (/* binding */ f),
/* harmony export */   sendHeightOnLoad: () => (/* binding */ s),
/* harmony export */   sendHeightOnPoll: () => (/* binding */ u),
/* harmony export */   sendHeightOnResize: () => (/* binding */ c)
/* harmony export */ });
const t=/xPYMx/;function n(n){function e(e){if(e.source!==n.contentWindow)return;const{data:i}=e;if("amp"===i.sentinel&&"embed-size"===i.type)n.setAttribute("height",i.height);else if("string"==typeof i&&"pym"===i.slice(0,3)){const[,,e,o]=i.split(t);"height"===e&&n.setAttribute("height",o)}}return window.addEventListener("message",e,!1),n.contentWindow&&n.contentWindow.postMessage({sentinel:"amp",type:"frames-init"},"*"),function(){window.removeEventListener("message",e,!1)}}function e(t,{attributes:e,src:i}={}){const o=document.createElement("iframe"),a=n(o);if(i&&o.setAttribute("src",i),o.setAttribute("width","100%"),o.setAttribute("scrolling","no"),o.setAttribute("marginheight","0"),o.setAttribute("frameborder","0"),e)for(let t in e)o.setAttribute(t,e[t]);return t.appendChild(o),{remove(){a(),t.removeChild(o)}}}const i="data-frame-attribute-".length;function o(t){const n={},e=t.attributes,o=e.length;for(let t=0;t<o;t++){const o=e[t].name;"data-frame-attribute-"===o.slice(0,i)&&(n[o.slice(i)]=e[t].value)}return n}function a(){const t=document.querySelectorAll("[data-frame-src]:not([data-frame-auto-initialized])");for(let n=0;n<t.length;n++){const i=t[n],a=i.getAttribute("data-frame-src"),r=o(i);i.setAttribute("data-frame-auto-initialized",""),e(i,{attributes:r,src:a})}}function r(t=function(){return document.documentElement.offsetHeight}()){window.parent.postMessage({sentinel:"amp",type:"embed-size",height:t},"*")}function s(){window.addEventListener("load",function t(){r(),window.removeEventListener("load",t,!1)},!1)}function c(){window.addEventListener("resize",()=>r(),!1)}function f(){window.addEventListener("message",function t(n){const{data:e}=n;"amp"===e.sentinel&&"frames-init"===e.type&&(window.removeEventListener("message",t,!1),r())},!1)}function u(t=300){setInterval(r,t)}function d(){r(),s(),c(),f()}function m(t){d(),u(t)}
//# sourceMappingURL=frames.modern.js.map


/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
/******/ 	/* webpack/runtime/define property getters */
/******/ 	(() => {
/******/ 		// define getter functions for harmony exports
/******/ 		__webpack_require__.d = (exports, definition) => {
/******/ 			for(var key in definition) {
/******/ 				if(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {
/******/ 					Object.defineProperty(exports, key, { enumerable: true, get: definition[key] });
/******/ 				}
/******/ 			}
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/hasOwnProperty shorthand */
/******/ 	(() => {
/******/ 		__webpack_require__.o = (obj, prop) => (Object.prototype.hasOwnProperty.call(obj, prop))
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/make namespace object */
/******/ 	(() => {
/******/ 		// define __esModule on exports
/******/ 		__webpack_require__.r = (exports) => {
/******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 			}
/******/ 			Object.defineProperty(exports, '__esModule', { value: true });
/******/ 		};
/******/ 	})();
/******/ 	
/************************************************************************/
var __webpack_exports__ = {};
// This entry needs to be wrapped in an IIFE because it needs to be isolated against other modules in the chunk.
(() => {
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _newswire_frames__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(572);


(0,_newswire_frames__WEBPACK_IMPORTED_MODULE_0__.autoInitFrames)();

})();

/******/ })()
;