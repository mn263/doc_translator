var myApp = angular.module('myApp', []);


myApp.controller('FilesCtrl', function ($scope) {
  $scope.files = [
    {name: 'learn angular'},
    {name: 'build an angular app'}
  ];

  $scope.addFile = function () {
    $scope.files.push({text: $scope.fileText});
    $scope.fileText = '';
  };


});

myApp.directive('igLogin', function () {
  return {
    restrict: 'E',
    replace: true,
    template: '<button ng-click="toggleModal()" ng-click="loginClicked(this)" id="login-button" class="btn">Log In</button>',
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

      $scope.modalShown = false;
      $scope.toggleModal = function () {
        $scope.modalShown = !$scope.modalShown;
      };


    }
  };
});

myApp.directive('modalDialog', function () {
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
      scope.hideModal = function () {
        scope.show = false;
      };
    },
    template: "<div class='ng-modal' ng-show='show'> <div class='ng-modal-overlay' ng-click='hideModal()'></div> <div class='ng-modal-dialog' ng-style='dialogStyle'> <div class='ng-modal-close' ng-click='hideModal()'>X</div> <div class='ng-modal-dialog-content' ng-transclude></div> </div> </div>" // See below
  };
});