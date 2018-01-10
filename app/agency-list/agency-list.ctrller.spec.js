'use strict';

describe('AgencyListCtrller', function() {

        var $scope;
        var $q;
        var deferred;
        var $rootScope;

        var remoteAgencies = [{"name":"Name","description":"Description","grade":1,"tags":"tags"},
                {"name":"Name","description":"Description","grade":1,"tags":"tags"}]

        beforeEach(module('SLApp'));

        beforeEach(inject(function($controller, _$q_, _$rootScope_, SLService) {
                $q = _$q_;
                $rootScope = _$rootScope_;
                $scope = _$rootScope_.$new();
                deferred = _$q_.defer();

                // Use a Jasmine Spy to return the deferred promise
                spyOn(SLService, 'getAgencies').and.returnValue(deferred.promise);

                $controller('AgencyListCtrller', {$scope: $scope, SLService:SLService});
        }));

        it('should create a `agency` model with 0 agency', inject(function($controller) {
                deferred.resolve(remoteAgencies)

                $scope.$apply();

                expect($scope.agencies.length).toBe(remoteAgencies.length);
        }));

});