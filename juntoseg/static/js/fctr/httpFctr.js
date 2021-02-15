 challenge.factory('HttpFctr', function WsHttp($q, $http, $rootScope) {
    return function(apiUrl, method, infos){
        var q = $q.defer()
        infos = typeof infos == 'object' ? infos : {}
        params = typeof infos.params == 'object' ? infos.params : {}
        token = localStorage.getItem('token')
        var headers = {}
        if (token)
            headers['Authorization'] = `Bearer ${token}`
        
        console.log('tem token', headers.Authorization)
        $http({
            url: `/${apiUrl}/`,
            method: method,
            params: params,
            data: infos.data,
            responseType: 'json',
            headers: headers,
            timeout: q.promise,
        }).then(
            function(response){
                q.resolve(response.data)
            },
            function(error){
                if(error.xhrStatus != 'abort' && (error.data && !error.data.messages))
                    console.error('HttpFctr HTTP ERROR >> ',JSON.stringify(error))

                var field = Object.keys(error.data)[0]
                if (!(error.data[field] == '[object Object]')) 
                    window.errorMessage = `${field}: ${error.data[field]}`
                else
                    window.errorMessage = 'This field already exists in this instance'

                q.reject(error)
            }
        )
        return q.promise
    }
})
 