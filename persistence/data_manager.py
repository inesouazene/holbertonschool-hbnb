import json
import os
from datetime import datetime
from persistence.ipersistence_manager import IPersistenceManager

class DataManager(IPersistenceManager):
    """A class that manages the persistence of data in a JSON file."""

    def __init__(self):
        """Initialize the DataManager object."""
        self.file_path = "data.json"
        self._initialize_file()

    def _initialize_file(self):
        """Initialize the data file if it doesn't exist."""
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump({}, f)

    def _read_data(self):
        """Read the data from the file and return it as a dictionary."""
        self._initialize_file()
        with open(self.file_path, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}

    def _write_data(self, data):
        """Write the given data dictionary to the file."""
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def save(self, entity):
        """
        Save the given entity to the data file.

        Args:
            entity: The entity object to be saved.
        """
        self._initialize_file()
        data = self._read_data()
        entity_data = entity.to_dict()
        entity_type = entity.__class__.__name__
        entity_id = entity.id
        if entity_type not in data:
            data[entity_type] = {}
        data[entity_type][entity_id] = entity_data
        self._write_data(data)

    def get(self, entity_id, entity_type):
        """
        Retrieve the entity with the given ID and type from the data file.

        Args:
            entity_id: The ID of the entity to retrieve.
            entity_type: The type of the entity to retrieve.

        Returns:
            The entity with the given ID and type, or None if not found.
        """
        self._initialize_file()
        data = self._read_data()
        return data.get(entity_type, {}).get(entity_id)

    def update(self, entity):
        """
        Update the given entity in the data file.

        Args:
            entity: The entity object to be updated.
        """
        self.save(entity)

    def delete(self, entity_id, entity_type):
        """
        Delete the entity with the given ID and type from the data file.

        Args:
            entity_id: The ID of the entity to delete.
            entity_type: The type of the entity to delete.
        """
        self._initialize_file()
        data = self._read_data()
        if entity_type in data and entity_id in data[entity_type]:
            del data[entity_type][entity_id]
            self._write_data(data)

    def get_all(self, entity_type):
        """
        Retrieve all entities of the given type from the data file.

        Args:
            entity_type: The type of the entities to retrieve.

        Returns:
            A list of all entities of the given type.
        """
        self._initialize_file()
        data = self._read_data()
        return list(data.get(entity_type, {}).values())

    def clear(self, entity_type):
        """
        Clear all entities of the given type from the data file.

        Args:
            entity_type: The type of the entities to clear.
        """
        data = self._read_data()
        if entity_type in data:
            data[entity_type] = {}
            self._write_data(data)
