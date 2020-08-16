const db = firebase.firestore()

function check(){
    firebase.auth().onAuthStateChanged(function(user) {
        if (user) {
            document.getElementById("user-name").innerHTML = `Heyya ${user.displayName}!`
        } else {
            window.location.replace("/auth/")
        }
    })
}

function addToCart(e){
    firebase.auth().onAuthStateChanged(function(user) {
        if (user) {
            fetch(`/addtocart/?userkey=${user.uid}&image=${e.image}&name=${e.name}&description=${e.description}&price=${e.price}`)
            .then((response) => {
                console.log(response)
                window.location.replace("/cart/")
            }).catch((error) => {
                console.log(error)
            })
        } else {
            window.location.replace("/auth/")
        }
    })
}

function renderCart(doc){
    document.getElementById("name").innerHTML = doc.data().cart[0].name;
    document.getElementById("description").innerHTML = doc.data().cart[0].description;
    document.getElementById("price").innerHTML = `₹ ${doc.data().cart[0].price} /*`;
    document.getElementById("image").src = doc.data().cart[0].image;
}

function cart(){
    firebase.auth().onAuthStateChanged(function(user) {
        if (user) {
            db.collection("users").doc(user.uid).get().then((doc) => {
                renderCart(doc)
            })
        } else {
            window.location.replace("/auth/")
        }
    })
}

function renderCheckout(doc){
    document.getElementById("name").innerHTML = doc.data().cart[0].name;
    document.getElementById("price").innerHTML = `₹ ${doc.data().cart[0].price} /*`;
}

function checkDetails(){
    firebase.auth().onAuthStateChanged(function(user) {
        if (user) {
            db.collection("users").doc(user.uid).get().then((doc) => {
                renderCheckout(doc)
            })
        } else {
            window.location.replace("/auth/")
        }
    })
}

function enterCode(){
    document.getElementById("loading").innerHTML = "Loading..."
    firebase.auth().onAuthStateChanged(function(user) {
        if (user) {
            db.collection("users").doc(user.uid).get().then((doc) => {
                renderCheckout(doc)
                discount(doc.data().cart[0].price)
            })
        } else {
            window.location.replace("/auth/")
        }
    })
}

function discount(e){
    const code = document.getElementById("code").value
    if(code === "covid19"){
        document.getElementById("price").innerHTML = e - 40
        document.getElementById("discount").innerHTML = "- 40 (discount)"
        document.getElementById("message").innerHTML = "Coupon code applied!"
        document.getElementById("loading").innerHTML = ""
    } else {
        document.getElementById("message").innerHTML = "Wrong coupon code!"
        document.getElementById("discount").innerHTML = "- 0 (discount)"
        document.getElementById("loading").innerHTML = ""
    }
}

function confirmOrder(){
    document.getElementById("final-load").innerHTML = "Loading..."
    
    // ORDER INFO
    var name = document.getElementById("name").value
    var price = document.getElementById("price").value
    var address = document.getElementById("address").value
console.log("2")
    if(address.length === 0){
        document.getElementById("final-load").innerHTML = ""
        document.getElementById("req").innerHTML = "All fields are required"
    } else {
        document.getElementById("req").innerHTML = ""
        firebase.auth().onAuthStateChanged(function(user) {
            if (user) {
                fetch(`/ordernow/?userkey=${user.uid}&name=${name}&price=${price}&address=${address}&email=${user.email}`)
                .then((response) => {
                    window.location.replace("/success/")
                }).catch((error) => {
                    window.location.replace("/error/")
                })
            } else {
                window.location.replace("/auth/")
            }
        })
    }
}

function signout(){
    firebase.auth().signOut().then(function() {
        window.location.replace("/auth/")
    }).catch(function(error) {
        window.location.replace("/error/")
    });
}