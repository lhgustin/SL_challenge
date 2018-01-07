angular.module('SLApp')
    .service("SLService", function ($http, $q) {
            console.log('SLService init')

            var self = this
            var baseUrl = 'http://localhost:8080/'

            var apiGet = function (apiEndpoint) {
                    return function () {
                            console.log('apiGet '+apiEndpoint)
                            var deferred = $q.defer();
                            return $http.get(baseUrl+apiEndpoint)
                                .then(function (response) {
                                        console.log('apiGet '+apiEndpoint+' OK')
                                        console.log('apiGet '+apiEndpoint+' payload ='+JSON.stringify(response))
                                        deferred.resolve(response.data);
                                        return deferred.promise;
                                }, function (response) {
                                        console.log('apiGet '+apiEndpoint+' KO')
                                        deferred.reject(response);
                                        return deferred.promise;
                                });
                    }
            }

            var apiPost = function (apiEndpoint) {
                    return function (requestObj) {
                            console.log('apiPost '+apiEndpoint)
                            var deferred = $q.defer();
                            var jsonRequest = JSON.stringify(requestObj)
                            console.log('apiPost '+apiEndpoint+' request = '+jsonRequest)
                            var config = {headers: {'Content-Type': 'application/json'}}
                            return $http.post(baseUrl+apiEndpoint, jsonRequest, config)
                                .then(function (response) {
                                        console.log('apiPost '+apiEndpoint+' OK')
                                        console.log('apiPost '+apiEndpoint+' payload ='+JSON.stringify(response))
                                        deferred.resolve(response.data);
                                        return deferred.promise;
                                }, function (response) {
                                        console.log('apiPost '+apiEndpoint+' KO')
                                        deferred.reject(response);
                                        return deferred.promise;
                                });
                    }
            }

            /* global vars */
            self.gradeMapper = {
                            '0':'PADAWAN',
                            '1':'JEDI',
                            '2':'MASTER'
                    }

            self.gradeColorMapper = {
                            '0':'green',
                            '1':'orange',
                            '2':'red'
                    }

            /* services */
            self.getAgencies = apiGet('agencies')
            self.addAgency = apiPost('add_agency')
    });