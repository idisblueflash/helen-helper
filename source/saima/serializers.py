from django.core.serializers.json import Serializer


class AlfredSerializer(Serializer):
    def get_dump_object(self, obj):
        return {
            'uid': obj.id,
            'title': obj.description,
            'subtitle': obj.command,
            'arg': obj.command,
            'icon': { 'path': f'{obj.category}.png'}
        }

    def start_serialization(self):
        self.stream.write('{"items": ')
        super().start_serialization()

    def end_serialization(self):
        super().end_serialization()
        self.stream.write('}')
