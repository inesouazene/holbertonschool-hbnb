#!/usr/bin/python3

from abc import ABC, abstractmethod

class IPersistenceManager(ABC):
    """
    Interface pour la gestion de la persistence des données.
    """

    @abstractmethod
    def save(self, entity):
        """
        Méthode abstraite pour sauvegarder une entité.
        """
        pass

    @abstractmethod
    def get(self, entity_id, entity_type):
        """
        Méthode abstraite pour récupérer une entité par son ID et son type.
        """
        pass

    @abstractmethod
    def update(self, entity):
        """
        Méthode abstraite pour mettre à jour une entité.
        """
        pass

    @abstractmethod
    def delete(self, entity_id, entity_type):
        """
        Méthode abstraite pour supprimer une entité par son ID et son type.
        """
        pass
