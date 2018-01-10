'use strict';

describe('AgencyCreatorCtrller', function() {

        var $scope;
        var $q;
        var deferred;
        var $rootScope;

        beforeEach(module('SLApp'));

        beforeEach(inject(function($controller, _$q_, _$rootScope_, SLService, _$mdDialog_, _$mdToast_) {
                $q = _$q_;
                $rootScope = _$rootScope_;
                $scope = _$rootScope_.$new();
                $scope.agencies = SLService.agencies; // like from SLService
                deferred = _$q_.defer();

                // Use a Jasmine Spy to return the deferred promise - decorate with a mock
                spyOn(SLService, 'addAgency').and.callFake(function (agencyJson) {
                        console.log('call fake'+JSON.stringify(agencyJson))
                        return deferred.promise
                });

                $controller('AgencyCreatorCtrller', {$scope: $scope, SLService:SLService, $mdDialog:_$mdDialog_, $mdToast:_$mdToast_});
        }));

        it('should create a `agency` model with 1 agency', inject(function($controller) {
                deferred.resolve('ok')

                // form filled
                $scope.addModel = {
                        name:'Name',
                        description:'Description',
                        tags:'tags',
                        grade:1
                }

                // simulate click
                $scope.addAgency()

                // apply last scope change (deferred)
                $scope.$apply();

                expect($scope.agencies.length).toBe(1);
        }));

});