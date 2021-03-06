from rest_framework import serializers
from bbncreative_cms.models import (
    Collaborator,
    Credit,
    Feed,
    Project,
    TextAsset,
    ImageAsset,
    EmbeddedAsset,
)


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    def to_representation(self, instance):
        original = super().to_representation(instance)

        return {
            "id": original["id"],
            "name": original["name"],
            "shortName": original["menu_name"],
            "description": original["bio"],
            "slug": original["url_name"],
            "progress": {
                "complete": original["is_complete"],
                "date": original["date_complete"],
            },
            "clientName": original["client_name"],
            "images": {"icon": original["icon"], "hero": original["hero"]},
            "colors": {
                "primary": original["brand_color_1"],
                "secondary": original["brand_color_2"],
            },
            "callToAction": {
                "label": original["cta_title"],
                "url": original["cta_url"],
            },
        }

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "menu_name",
            "bio",
            "url_name",
            "date_complete",
            "is_complete",
            "cta_title",
            "cta_url",
            "client_name",
            "icon",
            "hero",
            "brand_color_1",
            "brand_color_2",
        ]


class FeedSerializer(serializers.HyperlinkedModelSerializer):
    def to_representation(self, instance):
        original = super().to_representation(instance)

        return {
            "id": original["id"],
            "name": original["name"],
            "shortName": original["menu_name"],
            "description": original["bio"],
            "slug": original["url_name"],
            "lastUpdated": original["date_time_updated"],
            "icon": {"faName": original["menu_icon_name"],},
            "protected": original["protected"],
            "permanent": original["permanent"],
            "images": {"hero": original["hero"]},
            "colors": {
                "primary": original["brand_color_1"],
                "secondary": original["brand_color_2"],
            },
        }

    class Meta:
        model = Feed
        fields = [
            "id",
            "name",
            "menu_name",
            "bio",
            "url_name",
            "date_time_updated",
            "menu_icon_name",
            "protected",
            "permanent",
            "hero",
            "brand_color_1",
            "brand_color_2",
        ]


class CollaboratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborator
        fields = ["name", "url", "twitter"]


class CreditSerializer(serializers.ModelSerializer):
    collaborator = CollaboratorSerializer(read_only=True)

    class Meta:
        model = Credit
        fields = ["action", "collaborator"]


class TextAssetSerializer(serializers.ModelSerializer):
    # Re-orders attributes to match other assets
    def to_representation(self, instance):
        original = super().to_representation(instance)

        return {
            "id": original["id"],
            "parent": original["parent"],
            "created_at": original["created_at"],
            "title": original["title"],
            "body": original["body"],
            "importance": original["importance"],
        }

    class Meta:
        model = TextAsset
        exclude = ["feeds"]


class ImageAssetSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        original = super().to_representation(instance)

        return {
            "id": original["id"],
            "parent": original["parent"],
            "created_at": original["created_at"],
            "title": original["title"],
            "body": original["body"],
            "importance": original["importance"],
            "content": {
                "src": original["img"],
                "alt": original["alt"],
                "ratio": original["aspect_ratio"],
            },
        }

    class Meta:
        model = ImageAsset
        exclude = ["feeds"]


class EmbeddedAssetSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        original = super().to_representation(instance)

        return {
            "id": original["id"],
            "parent": original["parent"],
            "created_at": original["created_at"],
            "title": original["title"],
            "body": original["body"],
            "importance": original["importance"],
            "content": {
                "code": original["embed_code"],
                "ratio": original["aspect_ratio"],
            },
        }

    class Meta:
        model = EmbeddedAsset
        exclude = ["feeds"]
