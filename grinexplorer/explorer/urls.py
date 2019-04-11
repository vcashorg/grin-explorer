from django.urls import path

from .views import BlockList, BlocksByHeight, BlockDetail, Search
from .charts import block_chart, fee_chart
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", BlockList.as_view(), name="block-list"),
    path("chart/block", block_chart, name="block-chart"),
    path("chart/fee", fee_chart, name="fee-chart"),
    path("block/<int:height>", BlocksByHeight.as_view(), name="blocks-by-height"),
    path("block/<str:pk>", BlockDetail.as_view(), name="block-detail"),
    path("search", Search.as_view(), name="search"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
