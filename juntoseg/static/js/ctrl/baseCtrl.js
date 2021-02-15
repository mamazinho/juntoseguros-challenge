challenge.controller('BaseCtrl', function($scope, $rootScope){

    $scope.__init__ = function(){
      $rootScope.accessToken = localStorage.getItem('token') || ''
      $rootScope.refreshToken = ''
      $rootScope.active_tab = ''
      window.errorMessage = ''

      $scope.$on('changeTab', (event, data) => {
        if ($rootScope.accessToken)
          $scope.active_tab = 'dashboard'
        else
          $scope.active_tab = data
      })
      $scope.$on('setToken', (event, data) => {
        tokens = JSON.parse(data.tokens)
        $rootScope.accessToken = tokens.access
        $rootScope.refreshToken = tokens.refresh
        localStorage.setItem('token', $rootScope.accessToken)
      })
      $scope.$on('logout', (event, data) => {
        $rootScope.accessToken = ''
        $rootScope.refreshToken = ''
        localStorage.removeItem('token')
        $scope.$emit('changeTab', 'login')
      })

      $scope.$emit('changeTab', 'login')
    }
  
    $scope.__init__()
  
  })
  