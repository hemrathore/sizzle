var ui = new firebaseui.auth.AuthUI(firebase.auth());

var uiConfig = {
    callbacks: {
        signInSuccessWithAuthResult: function(authResult, redirectUrl) { 
            firebase.auth().onAuthStateChanged(function(user) {
                if (user) {
                    fetch(`/adduser/?userkey=${user.uid}&name=${user.displayName}&email=${user.email}`, {
                        method: 'GET',
                    })
                    .then(response => response.json())
                    .then(data => {
                        window.location.replace("/catalog/")
                    })
                    .catch((error) => {
                        window.location.replace("/catalog/")
                    })
                } else {
                    //
                }
            })
        },
        uiShown: function() {
            document.getElementById('loader').style.display = 'none';
        }
    },
    signInFlow: 'redirect',
    signInOptions: [
        firebase.auth.GoogleAuthProvider.PROVIDER_ID,
        firebase.auth.EmailAuthProvider.PROVIDER_ID,
    ],
};

ui.start('#firebaseui-auth-container', uiConfig);