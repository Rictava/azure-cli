# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals
# pylint: disable=bad-continuation
# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType
from ..generated._client_factory import (
    cf_kusto_operation,
    cf_kusto_pool,
    cf_kusto_pool,
    cf_kusto_pool_attached_database_configuration,
    cf_kusto_pool_database,
    cf_kusto_pool_data_connection,
    cf_kusto_pool_principal_assignment,
    cf_kusto_pool_database_principal_assignment,
)


synapse_kusto_pool_attached_database_configuration = CliCommandType(
    operations_tmpl='azure.mgmt.synapse.operations._kusto_pool_attached_database_configurations_operations#KustoPoolAttachedDatabaseConfigurationsOperations.{}',
    client_factory=cf_kusto_pool_attached_database_configuration,
)


synapse_kusto_pool_data_connection = CliCommandType(
    operations_tmpl=(
        'azure.mgmt.synapse.operations._kusto_pool_data_connections_operations#KustoPoolDataConnectionsOperations.{}'
    ),
    client_factory=cf_kusto_pool_data_connection,
)


synapse_kusto_pool_database = CliCommandType(
    operations_tmpl='azure.mgmt.synapse.operations._kusto_pool_databases_operations#KustoPoolDatabasesOperations.{}',
    client_factory=cf_kusto_pool_database,
)


synapse_kusto_pool_database_principal_assignment = CliCommandType(
    operations_tmpl='azure.mgmt.synapse.operations._kusto_pool_database_principal_assignments_operations#KustoPoolDatabasePrincipalAssignmentsOperations.{}',
    client_factory=cf_kusto_pool_database_principal_assignment,
)


synapse_kusto_pool = CliCommandType(
    operations_tmpl='azure.mgmt.synapse.operations._kusto_pool_operations#KustoPoolOperations.{}',
    client_factory=cf_kusto_pool,
)


synapse_kusto_pool = CliCommandType(
    operations_tmpl='azure.mgmt.synapse.operations._kusto_pools_operations#KustoPoolsOperations.{}',
    client_factory=cf_kusto_pool,
)


synapse_kusto_pool_principal_assignment = CliCommandType(
    operations_tmpl='azure.mgmt.synapse.operations._kusto_pool_principal_assignments_operations#KustoPoolPrincipalAssignmentsOperations.{}',
    client_factory=cf_kusto_pool_principal_assignment,
)


synapse_kusto_operation = CliCommandType(
    operations_tmpl='azure.mgmt.synapse.operations._kusto_operations_operations#KustoOperationsOperations.{}',
    client_factory=cf_kusto_operation,
)


def load_command_table(self, _):

    with self.command_group(
        'synapse kusto attached-database-configuration',
        synapse_kusto_pool_attached_database_configuration,
        client_factory=cf_kusto_pool_attached_database_configuration,
        is_experimental=True,
    ) as g:
        g.custom_command('list', 'synapse_kusto_attached_database_configuration_list')
        g.custom_show_command('show', 'synapse_kusto_attached_database_configuration_show')
        g.custom_command('create', 'synapse_kusto_attached_database_configuration_create', supports_no_wait=True)
        g.generic_update_command(
            'update',
            supports_no_wait=True,
            custom_func_name='synapse_kusto_attached_database_configuration_update',
            setter_name='begin_create_or_update',
        )
        g.custom_command(
            'delete', 'synapse_kusto_attached_database_configuration_delete', supports_no_wait=True, confirmation=True
        )
        g.custom_wait_command('wait', 'synapse_kusto_attached_database_configuration_show')

    with self.command_group(
        'synapse kusto data-connection',
        synapse_kusto_pool_data_connection,
        client_factory=cf_kusto_pool_data_connection,
        is_experimental=True,
    ) as g:
        g.custom_command('list', 'synapse_kusto_data_connection_list')
        g.custom_show_command('show', 'synapse_kusto_data_connection_show')
        g.custom_command('event-grid create', 'synapse_kusto_data_connection_event_grid_create', supports_no_wait=True)
        g.custom_command('event-hub create', 'synapse_kusto_data_connection_event_hub_create', supports_no_wait=True)
        g.custom_command('iot-hub create', 'synapse_kusto_data_connection_iot_hub_create', supports_no_wait=True)
        g.custom_command('event-grid update', 'synapse_kusto_data_connection_event_grid_update', supports_no_wait=True)
        g.custom_command('event-hub update', 'synapse_kusto_data_connection_event_hub_update', supports_no_wait=True)
        g.custom_command('iot-hub update', 'synapse_kusto_data_connection_iot_hub_update', supports_no_wait=True)
        g.custom_command('delete', 'synapse_kusto_data_connection_delete', supports_no_wait=True, confirmation=True)
        g.custom_wait_command('wait', 'synapse_kusto_data_connection_show')

    with self.command_group(
        'synapse kusto database',
        synapse_kusto_pool_database,
        client_factory=cf_kusto_pool_database,
        is_experimental=True,
    ) as g:
        g.custom_command('list', 'synapse_kusto_database_list')
        g.custom_show_command('show', 'synapse_kusto_database_show')
        g.custom_command('create', 'synapse_kusto_database_create', supports_no_wait=True)
        g.custom_command('update', 'synapse_kusto_database_update', supports_no_wait=True)
        g.custom_command('delete', 'synapse_kusto_database_delete', supports_no_wait=True, confirmation=True)
        g.custom_wait_command('wait', 'synapse_kusto_database_show')

    with self.command_group(
        'synapse kusto database-principal-assignment',
        synapse_kusto_pool_database_principal_assignment,
        client_factory=cf_kusto_pool_database_principal_assignment,
        is_experimental=True,
    ) as g:
        g.custom_command('list', 'synapse_kusto_database_principal_assignment_list')
        g.custom_show_command('show', 'synapse_kusto_database_principal_assignment_show')
        g.custom_command('create', 'synapse_kusto_database_principal_assignment_create', supports_no_wait=True)
        g.generic_update_command(
            'update',
            supports_no_wait=True,
            custom_func_name='synapse_kusto_database_principal_assignment_update',
            setter_name='begin_create_or_update',
        )
        g.custom_command(
            'delete', 'synapse_kusto_database_principal_assignment_delete', supports_no_wait=True, confirmation=True
        )
        g.custom_wait_command('wait', 'synapse_kusto_database_principal_assignment_show')

    with self.command_group(
        'synapse kusto pool', synapse_kusto_pool, client_factory=cf_kusto_pool, is_experimental=True
    ) as g:
        g.custom_command('list-sku', 'synapse_kusto_pool_list_sku')

    with self.command_group(
        'synapse kusto pool', synapse_kusto_pool, client_factory=cf_kusto_pool, is_experimental=True
    ) as g:
        g.custom_command('list', 'synapse_kusto_pool_list')
        g.custom_show_command('show', 'synapse_kusto_pool_show')
        g.custom_command('delete', 'synapse_kusto_pool_delete', supports_no_wait=True, confirmation=True)
        g.custom_command('list-follower-database', 'synapse_kusto_pool_list_follower_database')
        g.custom_command('list-language-extension', 'synapse_kusto_pool_list_language_extension')
        g.custom_command('list-sku', 'synapse_kusto_pool_list_sku')
        g.custom_command('start', 'synapse_kusto_pool_start', supports_no_wait=True)
        g.custom_command('stop', 'synapse_kusto_pool_stop', supports_no_wait=True)
        g.custom_wait_command('wait', 'synapse_kusto_pool_show')

    with self.command_group(
        'synapse kusto pool-principal-assignment',
        synapse_kusto_pool_principal_assignment,
        client_factory=cf_kusto_pool_principal_assignment,
        is_experimental=True,
    ) as g:
        g.custom_command('list', 'synapse_kusto_pool_principal_assignment_list')
        g.custom_show_command('show', 'synapse_kusto_pool_principal_assignment_show')
        g.custom_command('create', 'synapse_kusto_pool_principal_assignment_create', supports_no_wait=True)
        g.generic_update_command(
            'update',
            supports_no_wait=True,
            custom_func_name='synapse_kusto_pool_principal_assignment_update',
            setter_name='begin_create_or_update',
        )
        g.custom_command(
            'delete', 'synapse_kusto_pool_principal_assignment_delete', supports_no_wait=True, confirmation=True
        )
        g.custom_wait_command('wait', 'synapse_kusto_pool_principal_assignment_show')

    with self.command_group(
        'synapse kusto-operation', synapse_kusto_operation, client_factory=cf_kusto_operation, is_experimental=True
    ) as g:
        g.custom_command('list', 'synapse_kusto_operation_list')