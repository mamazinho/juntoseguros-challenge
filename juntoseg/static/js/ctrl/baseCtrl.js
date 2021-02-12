challenge.controller('BaseCtrl', function($scope, $rootScope){

    $scope.__init__ = function(){
      $rootScope.active_tab = 'login'
      $rootScope.username = ''
      $rootScope.email = ''
      $rootScope.accessToken = ''
      $rootScope.refreshToken = ''
      window.errorMessage = ''
      $scope.$on('changeTab', (event, data) => {
        $scope.active_tab = data
      })
      $scope.$on('setToken', (event, data) => {
        $rootScope.email = data.email
        $rootScope.username = data.name
        tokens = JSON.parse(data.tokens)
        $rootScope.accessToken = tokens.access
        $rootScope.refreshToken = tokens.refresh
        localStorage.setItem('token', $rootScope.accessToken)
      })
    }
  
    $scope.__init__()
  
  })
  