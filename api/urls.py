from django.urls import path
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import AllowAny

from api.authentication import SafeJWTAuthentication
from api.views import CategoryViews, ProductViews, UserViews, GroupViews, CommentsViews, CartViews

urlpatterns = [
    # GROUPS
    path("group/create_group/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(GroupViews.CreateGroupView)).as_view()),
    path("group/delete_group_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(GroupViews.DeleteGroupByIdView)).as_view()),
    path("group/update_group_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(GroupViews.UpdateGroupByIdView)).as_view()),
    path("group/find_all_groups/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(GroupViews.GetGroupView)).as_view()),
    path("group/find_group_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(GroupViews.FindGroupByIdView)).as_view()),

    # USERS
    path("user/access_token/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.AccessToken)).as_view()),
    path("user/refresh_token/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.RefreshToken)).as_view()),
    path("user/registration/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.UserRegistrationView)).as_view()),
    path("user/create_super_user/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.CreateSuperUserView)).as_view()),
    path("user/delete_user_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.DeleteUserByIdView)).as_view()),
    path("user/delete_all_users/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.DeleteAllUsersView)).as_view()),
    path("user/update_user_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.UpdateUserView)).as_view()),
    path("user/find_all_users/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.GetUserView)).as_view()),
    path("user/find_user_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(UserViews.FindUserByIdView)).as_view()),

    # CATEGORIES
    path("category/create_category/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(CategoryViews.CreateCategoryView)).as_view()),
    path("category/delete_category_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(CategoryViews.DeleteCategoryByIdView)).as_view()),
    path("category/update_category_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(CategoryViews.UpdateCategoryByIdView)).as_view()),
    path("category/find_all_categories/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(CategoryViews.GetCategoryView)).as_view()),
    path("category/find_category_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(CategoryViews.FindCategoryByIdView)).as_view()),

    # PRODUCTS
    path("product/create_product/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(ProductViews.CreateProductView)).as_view()),
    path("product/delete_product_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(ProductViews.DeleteProductByIdView)).as_view()),
    path("product/delete_all_products/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(ProductViews.DeleteAllProductView)).as_view()),
    path("product/update_product_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(ProductViews.UpdateProductByIdView)).as_view()),
    path("product/find_all_products/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(ProductViews.GetProductView)).as_view()),
    path("product/find_product_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(ProductViews.FindProductByIdView)).as_view()),

    # COMMENTS
    path("comments/create_comment/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(CommentsViews.CreateCommentView)).as_view()),
    path("comments/create_relplies/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(CommentsViews.CreateRelpliesView)).as_view()),
    path("comments/delete_comment_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(CommentsViews.DeleteCommentByIdView)).as_view()),
    path("comments/update_comment_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(CommentsViews.UpdateCommentByIdView)).as_view()),
    path("comments/find_all_comments/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(CommentsViews.GetCommentView)).as_view()),
    path("comments/find_comment_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(CommentsViews.FindCommentByIdView)).as_view()),

    # CART
    path("cart/create_cart/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(CartViews.CreateCartView)).as_view()),
    path("cart/delete_cart_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(CartViews.DeleteCartByIdView)).as_view()),
    path("cart/update_cart_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(CartViews.UpdateCartByIdView)).as_view()),
    path("cart/find_all_carts/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(CartViews.GetCartView)).as_view()),
    path("cart/find_cart_by_id/<int:pk>/",
         authentication_classes([SafeJWTAuthentication])(
             permission_classes([AllowAny])(CartViews.FindCartByIdView)).as_view()),

    # ORDERS

    # PRODUCT_HISTORY
]
