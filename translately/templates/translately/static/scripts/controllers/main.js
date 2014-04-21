var myApp = angular.module('myApp', []);


myApp.controller('FilesCtrl', function ($scope, $http) {//, $timeout, $route, $location) {
    $scope.File = {id: 0, title: 'learn angular', text: "THIS IS THE FIRST FILE"};
    $scope.Title = "TITLE";
    $scope.Words = $scope.File.text.split(" ");

    $scope.files = [
    ];

    $scope.translate = function(word) {
        var spinner = document.getElementById('loading-icon');
        spinner.style.visibility = "visible";
        var api = "https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20140421T003851Z.b2eb524b27906976.bd68efdbfba928829474912bb55c3cf970953e41&lang=es-en&text=" + word;
        var api2 = "https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20140421T003851Z.b2eb524b27906976.bd68efdbfba928829474912bb55c3cf970953e41&lang=en-es&text=" + word;
        $http({
            method: 'GET',
            url: api,
            headers: {'Content-type': 'application/json'}
        }).success( function( data ) {
            //if successful translate again
            var firstWord = data.text[0];
            $http({
                method: 'GET',
                url: api2,
                headers: {'Content-type': 'application/json'}
            }).success( function( data ) {
                spinner.style.visibility = "hidden";
                var secondWord = data.text[0];
                alert(firstWord + " -- " +secondWord);
            }).error( function() {
                spinner.style.visibility = "hidden";
            });
        }).error( function() {
            spinner.style.visibility = "hidden";
            alert("ERROR -- Failed AJAX");
        });
    };

    $scope.addFile = function () {
        $scope.files.push({text: $scope.fileText});
        $scope.fileText = '';
    };

    $scope.openFile = function (file) {
        $scope.File = file;
        $scope.Title = file.title;
        $scope.Words = file.text.split(" ");
    };

    $scope.signOut = function () {
        document.getElementById('login-button').style.visibility = "visible";
        document.getElementById('logout-button').style.visibility = "hidden";
        document.getElementById('login-username').value = "";
        document.getElementById('login-password').value = "";
        $scope.files = [ ];
    };

    $scope.login = function() {
        var username = document.getElementById('login-username').value;
        var password = document.getElementById('login-password').value;
        var api = "api/user-auth/";
        $http({
            method: 'POST',
            url: api,
            data: JSON.stringify({ username : username , password : password }),
            headers: {'Content-type': 'application/json'}
        }).success( function( data ) {
            if (data.authorization == 'verified') {
//                Close modal window
                $scope.$$childHead.hideModalLogin();
                document.getElementById('login-button').style.visibility = "hidden";
                document.getElementById('logout-button').style.visibility = "visible";
//                Get all of the person's documents
                $scope.loadDocuments();

            } else {
                alert("Invalid Login credentials.")
            }
        }).error( function() {
            alert("ERROR -- Check your credentials");
        });
    };

    $scope.signup = function() {
        var username = document.getElementById('signup-username').value;
        var email = document.getElementById('signup-email').value;
        var password = document.getElementById('signup-password').value;
        var passwordConfirm = document.getElementById('signup-password-confirm').value;
        var api = "api/user-create/";
        if(password != passwordConfirm) {
            alert("Passwords do not match");
            return;
        }
        $http({
            method: 'POST',
            url: api,
            data: JSON.stringify({ username : username, email: email, password : password }),
            headers: {'Content-type': 'application/json'}
        }).success( function( data ) {
            if (data.user == 'created') {
//                Close modal window
                $scope.$$childHead.$$nextSibling.$$nextSibling.hideModalSignup();
                document.getElementById('login-button').style.visibility = "hidden";
                document.getElementById('logout-button').style.visibility = "visible";
                document.getElementById('login-username').value = username;
                document.getElementById('login-password').value = password;
//                Get all of the person's documents
                $scope.loadDocuments();

            } else {
                alert("Invalid Login credentials.")
            }
        }).error( function() {
            alert("ERROR -- Are you using a valid email?");
        });
    };


    $scope.loadDocuments = function() {
        var username = document.getElementById('login-username').value;
        var password = document.getElementById('login-password').value;

        var api = "api/documents-get/username=" + username + "/password=" + password + "?format=json";
        $http({
            method: 'GET',
            url: api,
            headers: {'Content-type': 'application/json'}
        }).success( function( data ) {
            $scope.files = [ ];
            for (var i = 0; i < data.length; i++) {
                var title = data[i].title;
                var text = data[i].text;
                var id = data[i].id;
                var doc = {id: id, title: title, text: text};
                $scope.files.push(doc);
            }
        }).error( function() {
            alert("ERROR -- Are you logged in?");
        });
    };

    $scope.deleteFile = function (file) {
        var r=confirm("Are you sure you want to delete that file?");
        if (r==false) {
            return;
        }
        var username = document.getElementById('login-username').value;
        var password = document.getElementById('login-password').value;
        var docId = file.id;
        var api = "api/document-delete/";
        $http({
            method: 'DELETE',
            url: api,
            data: JSON.stringify({ username : username , password : password, document_id: docId }),
            headers: {'Content-type': 'application/json'}
        }).success( function( data ) {
            $scope.loadDocuments();
        }).error( function() {
            alert("ERROR -- Are you logged in?");
        });    };


    $scope.saveDocument = function(title, doc) {
        var username = document.getElementById('login-username').value;
        var password = document.getElementById('login-password').value;
        var api = "api/document-add/";
        $http({
            method: 'POST',
            url: api,
            data: JSON.stringify({ username : username , password : password, language: "English", title: title, text: doc }),
            headers: {'Content-type': 'application/json'}
        }).success( function( data ) {
            $scope.loadDocuments();
        }).error( function() {
            alert("ERROR -- Are you logged in?");
        });
    };


    function readBlob(opt_startByte, opt_stopByte) {
//        var spinner = document.getElementById('loading-icon');
//        spinner.style.visibility = "visible";

        var files = document.getElementById('files').files;
        if (!files.length) {
            alert('No file selected!');
            return;
        }
        var file = files[0];
        var start = parseInt(opt_startByte) || 0;
        var stop = parseInt(opt_stopByte) || file.size - 1;
        var title = file.name;
        var reader = new FileReader();
        // If we use onloadend, we need to check the readyState.
        reader.onloadend = function (evt) {
            if (evt.target.readyState == FileReader.DONE) { // DONE == 2
                $scope.saveDocument(title, evt.target.result);
            }
        };

        var blob = file.slice(start, stop + 1);
        reader.readAsBinaryString(blob);
//        spinner.style.visibility = "hidden";

    }

    $scope.readFile = function () {
        var startByte = document.getElementById('data-startbyte');
        var endByte = document.getElementById('data-endbyte');
        readBlob(startByte, endByte);
        document.getElementById("files").value = "";
    };

});

myApp.directive('igLogin', function () {
    return {
        restrict: 'E',
        replace: false,
        template: '<button ng-click="toggleLoginModal()" ng-click="loginClicked(this)" id="login-button" class="btn">Login</button>' +
            '<button ng-click="toggleSignupModal()" style="visibility: hidden;" id="signup-button-hidden"></button>',
        controller: function ($scope) {

            $scope.loggedIn = false;
            $scope.loginClicked = function (btn) {
                if ($scope.loggedIn) {
                    btn.value = "Sign In";
                    alert("You are logging out!");
                    $scope.loggedIn = false;
                } else {
                    btn.value = "Sign Out";
                    alert("You are logging in!");
                    $scope.loggedIn = true;
                }
            };

            $scope.loginShown = false;
            $scope.toggleLoginModal = function () {
                $scope.loginShown = !$scope.loginShown;
            };
        }
    };
});

myApp.directive('igSignup', function () {
    return {
        restrict: 'E',
        replace: false,
        template: '<button ng-click="toggleSignupModal()" style="visibility: hidden;" id="signup-button-hidden"></button>',
        controller: function ($scope) {
            $scope.signupShown = false;
            $scope.toggleSignupModal = function () {
                $scope.signupShown = !$scope.signupShown;
            };
        }
    };
});

myApp.directive('igDocument', function () {
    return {
        restrict: 'E',
        replace: false,
        template: '<button ng-click="toggleDocumentModal()" id="document-button-hidden" style="visibility: hidden"></button>',
        controller: function ($scope) {
            $scope.signupShown = false;
            $scope.toggleDocumentModal = function () {
                $scope.documentShown = !$scope.documentShown;
            };
        }
    };
});

myApp.directive('modalLogin', function () {
    return {
        restrict: 'E',
        scope: {
            show: '='
        },
        replace: true, // Replace with the template below
        transclude: true, // we want to insert custom content inside the directive
        link: function (scope, element, attrs) {
            scope.dialogStyle = {};
            if (attrs.width)
                scope.dialogStyle.width = attrs.width;
            if (attrs.height)
                scope.dialogStyle.height = attrs.height;
            scope.hideModalLogin = function () {
                scope.show = false;
            };
        },
        template: "<div class='ng-modal' ng-show='show'> <div class='ng-modal-overlay' ng-click='hideModalLogin()'></div> <div class='ng-modal-dialog' ng-style='dialogStyle'> <div class='ng-modal-close' ng-click='hideModalLogin()'>X</div> <div class='ng-modal-dialog-content' ng-transclude></div> </div> </div>" // See below
    };
});

myApp.directive('modalSignup', function () {
    return {
        restrict: 'E',
        scope: {
            show: '='
        },
        replace: true, // Replace with the template below
        transclude: true, // we want to insert custom content inside the directive
        link: function (scope, element, attrs) {
            scope.dialogStyle = {};
            if (attrs.width)
                scope.dialogStyle.width = attrs.width;
            if (attrs.height)
                scope.dialogStyle.height = attrs.height;
            scope.hideModalSignup = function () {
                scope.show = false;
            };
        },
        template: "<div class='ng-modal' ng-show='show'> <div class='ng-modal-overlay' ng-click='hideModalSignup()'></div> <div class='ng-modal-dialog' ng-style='dialogStyle'> <div class='ng-modal-close' ng-click='hideModalSignup()'>X</div> <div class='ng-modal-dialog-content' ng-transclude></div> </div> </div>" // See below
    };
});



myApp.directive('modalDocument', function () {
    return {
        restrict: 'E',
        scope: {
            show: '='
        },
        replace: true, // Replace with the template below
        transclude: true, // we want to insert custom content inside the directive
        link: function (scope, element, attrs) {
            scope.dialogStyle = {};
            if (attrs.width)
                scope.dialogStyle.width = attrs.width;
            if (attrs.height)
                scope.dialogStyle.height = attrs.height;
            scope.hideModalDocument = function () {
                scope.show = false;
            };
        },
        template: "<div class='ng-modal' ng-show='show'> <div class='ng-modal-overlay' ng-click='hideModalDocument()'></div> <div class='ng-modal-dialog' ng-style='dialogStyle'> <div id='spinner-spot' class='ng-modal-close' ng-click='hideModalDocument()' style='padding-right: 20px;'>X</div> <div class='ng-modal-dialog-content' style='max-height: 320px; overflow-y: auto;' ng-transclude></div> </div> </div>" // See below
    };
});


function signUp() {
    document.getElementsByClassName('ng-modal-overlay')[0].click();
    document.getElementById('signup-button-hidden').click();
}

function openDocModal() {
    document.getElementById('document-button-hidden').click();
}


