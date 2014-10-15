/**
 * Created by renzo on 10/15/14.
 */
var rest = angular.module('rest', []);
rest.factory('CursoApi', function () {
    return {
        salvar: function (curso) {
            var obj = {};
            obj.success = function (fcnSucesso) {
                obj.fcnSucesso = fcnSucesso;
            };
            obj.error = function (fcnErro) {
                obj.fcnError = fcnErro;
            };

            setTimeout(function () {
                curso.id = 1;
                obj.fcnSucesso(curso);

            }, 1000);

            return obj;
        }
    };
});