function getAvailabilityColor(value){
    const hue = (value*100).toString(10);
    return ["hsl(",hue,",100%,50%)"].join("");
}

function setAvailabilityBar(id, ratio) {
    const productElem = document.getElementById(id).querySelector(".availability-bar-outer");
    const progressBar = productElem.querySelector(".availability-bar-inner");
    progressBar.style.width = 100 * ratio + "%";
    progressBar.style.backgroundColor = getAvailabilityColor(ratio);
}

function setAvailabilityBarsOfProducts() {
    const products = JSON.parse(document.getElementById("product-ratios").textContent);
    products.forEach(productStr => {
        const product = JSON.parse(productStr);
        setAvailabilityBar(product.id, product.ratio);
    });
}
