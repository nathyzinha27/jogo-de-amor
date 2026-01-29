const naoBtn = document.querySelector(".nao");

naoBtn.addEventListener("mouseover", () => {
    const largura = window.innerWidth - naoBtn.offsetWidth;
    const altura = window.innerHeight - naoBtn.offsetHeight;

    naoBtn.style.left = Math.random() * largura + "px";
    naoBtn.style.top = Math.random() * altura + "px";
});
