challenge.controller('LoginCtrl', function($scope, HttpFctr, $timeout){

  $scope.__init__ = function(){
    $scope.loginData = {
      'email': '',
      'password': '',
    }
  }

  $scope.login = () => {
    HttpFctr('login', 'POST', {data: $scope.loginData}).then((response) => {
      $scope.$emit('setToken', response)
      $scope.$emit('changeTab', 'dashboard')
    }).catch((error) => {
      console.log('Error >> ', error)
      alert(window.errorMessage)
    })
  }

  $scope.__init__()

})
