# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::Scheduler
  module Models
    #
    # Model object.
    #
    class JobCollectionProperties

      include MsRestAzure

      # @return [Sku] Gets or sets the SKU.
      attr_accessor :sku

      # @return [JobCollectionState] Gets or sets the state. Possible values
      # include: 'Enabled', 'Disabled', 'Suspended', 'Deleted'
      attr_accessor :state

      # @return [JobCollectionQuota] Gets or sets the job collection quota.
      attr_accessor :quota

      #
      # Validate the object. Throws ValidationError if validation fails.
      #
      def validate
        @sku.validate unless @sku.nil?
        @quota.validate unless @quota.nil?
      end

      #
      # Serializes given Model object into Ruby Hash.
      # @param object Model object to serialize.
      # @return [Hash] Serialized object in form of Ruby Hash.
      #
      def self.serialize_object(object)
        object.validate
        output_object = {}

        serialized_property = object.sku
        unless serialized_property.nil?
          serialized_property = Sku.serialize_object(serialized_property)
        end
        output_object['sku'] = serialized_property unless serialized_property.nil?

        serialized_property = object.state
        output_object['state'] = serialized_property unless serialized_property.nil?

        serialized_property = object.quota
        unless serialized_property.nil?
          serialized_property = JobCollectionQuota.serialize_object(serialized_property)
        end
        output_object['quota'] = serialized_property unless serialized_property.nil?

        output_object
      end

      #
      # Deserializes given Ruby Hash into Model object.
      # @param object [Hash] Ruby Hash object to deserialize.
      # @return [JobCollectionProperties] Deserialized object.
      #
      def self.deserialize_object(object)
        return if object.nil?
        output_object = JobCollectionProperties.new

        deserialized_property = object['sku']
        unless deserialized_property.nil?
          deserialized_property = Sku.deserialize_object(deserialized_property)
        end
        output_object.sku = deserialized_property

        deserialized_property = object['state']
        if (!deserialized_property.nil? && !deserialized_property.empty?)
          enum_is_valid = JobCollectionState.constants.any? { |e| JobCollectionState.const_get(e).to_s.downcase == deserialized_property.downcase }
          warn 'Enum JobCollectionState does not contain ' + deserialized_property.downcase + ', but was received from the server.' unless enum_is_valid
        end
        output_object.state = deserialized_property

        deserialized_property = object['quota']
        unless deserialized_property.nil?
          deserialized_property = JobCollectionQuota.deserialize_object(deserialized_property)
        end
        output_object.quota = deserialized_property

        output_object
      end
    end
  end
end