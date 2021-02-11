challenge.controller('LoginCtrl', function($scope, HttpFctr, $rootScope){

  $scope.__init__ = function(){
    $scope.loginData = {
      'email': '',
      'password': '',
    }
  }

  $scope.login = () => {
    HttpFctr('login', 'POST', $scope.loginData).then((response) => {
      console.log(response)
    })
  }

  $scope.__init__()

})
