from django.shortcuts import render

# Create your views here.
# new1:
@api_view(["GET"])
def shop_card_badge(request):
    authentication_classes = [JWTAuthentication]

    # Validate the token and get the user
    token = request.headers.get('Authorization').split()[1]
    jwt_auth = JWTAuthentication()
    try:
        validated_token = jwt_auth.get_validated_token(token)
        user = jwt_auth.get_user(validated_token)
    except InvalidToken:
        return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

    # Check if the user has a cart
    try:
        cart = ShoppingCart.objects.get(user=user)
    except ShoppingCart.DoesNotExist:
        return Response({"total_quantity": 0}, status=status.HTTP_200_OK)

    total_quantity = cart.quantity

    return Response({"total_quantity": total_quantity}, status=status.HTTP_200_OK)




@api_view(["GET"])
def get_shop_card(request):
    authentication_classes = [JWTAuthentication]

    # Validate the token and get the user
    token = request.headers.get('Authorization').split()[1]
    jwt_auth = JWTAuthentication()
    try:
        validated_token = jwt_auth.get_validated_token(token)
        user = jwt_auth.get_user(validated_token)
    except InvalidToken:
        return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

    # Check if the user has a cart
    try:
        cart = ShoppingCart.objects.get(user=user)
    except ShoppingCart.DoesNotExist:
        return Response({"items": [], "total_price": 0, "total_quantity": 0}, status=status.HTTP_200_OK)

    cart_items = CartItem.objects.filter(cart=cart)

    # Prepare the cart data
    cart_data = []
    total_price = 0
    total_quantity = 0

    for item in cart_items:
        product_color = item.product_color
        product = product_color.product
        product_info = product.information.first()
        image_url = None

        if product.image.exists():
            sorted_images = product.image.order_by('order')
            image_url = request.build_absolute_uri(sorted_images.first().file.url)

        item_data = {
            'product_id': product.id,
            'product_name': product.name,
            'price': product_color.price,
            'quantity': item.quantity,
            'image': image_url,
            'color_product_id': product_color.id
        }

        total_price += product_color.price * item.quantity
        total_quantity += 1
        cart_data.append(item_data)

    response_data = {
        'items': cart_data,
        'total_price': total_price,
        'total_quantity': total_quantity
    }
    return Response(response_data, status=status.HTTP_200_OK)



# Delete From Shopcart
@api_view(["POST"])
def remove_item(request):
    authentication_classes = [JWTAuthentication]

    # Validate the token and get the user
    token = request.headers.get('Authorization').split()[1]
    jwt_auth = JWTAuthentication()
    try:
        validated_token = jwt_auth.get_validated_token(token)
        user = jwt_auth.get_user(validated_token)
    except InvalidToken:
        return Response({'error': 'Invalid token!'}, status=status.HTTP_401_UNAUTHORIZED)

    product_id = request.data.get("product_id")
    quantity = request.data.get("quantity", 1)  # Default quantity is 1

    # Fetch product
    try:
        product = ProductColor.objects.get(id=product_id)
    except ProductColor.DoesNotExist:
        return Response({"error": "Product not found!"}, status=status.HTTP_400_BAD_REQUEST)

    # Check if the user has a cart
    try:
        shop_cart = ShoppingCart.objects.get(user=user)
    except ShoppingCart.DoesNotExist:
        return Response({"error": "Shopping cart not found!"}, status=status.HTTP_400_BAD_REQUEST)

    # Check if the item is in the cart
    try:
        cart_item = CartItem.objects.get(cart=shop_cart, product_color=product)
        if cart_item.quantity > quantity:
            cart_item.quantity -= quantity
            cart_item.save()
        else:
            cart_item.delete()
            shop_cart.quantity -= 1
            shop_cart.save()
    except CartItem.DoesNotExist:
        return Response({"error": "Item not found in cart!"}, status=status.HTTP_400_BAD_REQUEST)

    # Update the inventory
    product.inventory += quantity
    product.save()

    # Check if the cart is empty and remove it
    if not shop_cart.items.exists():
        shop_cart.delete()

    return Response({"success": "Item removed from cart"}, status=status.HTTP_200_OK)




# Add New Item To ShopCard

@api_view(["POST"])
def add_to_card(request):
    authentication_classes = [JWTAuthentication]

    # Validate the token and get the user
    token = request.headers.get('Authorization').split()[1]
    jwt_auth = JWTAuthentication()
    try:
        validated_token = jwt_auth.get_validated_token(token)
        user = jwt_auth.get_user(validated_token)
    except InvalidToken:
        return Response({'error': 'Invalid token!'}, status=status.HTTP_401_UNAUTHORIZED)
    product_id = request.data.get("product_id")
    quantity = request.data.get("quantity", 1)  # Default quantity is 1

    # Fetch product and user
    try:
        product = ProductColor.objects.get(id=product_id)
    except (Product.DoesNotExist):
        return Response({"error": "Product not found!"}, status=status.HTTP_400_BAD_REQUEST)
    if not product.inventory >= quantity:
        return Response({'error': "No inventory!"}, status=status.HTTP_400_BAD_REQUEST)
    product.inventory -= quantity
    product.save()

    # Check if the user has a cart
    try:
        shop_cart = ShoppingCart.objects.get(user=user)
        shop_cart.quantity += 1
        shop_cart.save()
    except ShoppingCart.DoesNotExist:
        # If user doesn't have a cart, create a new one
        shop_cart = ShoppingCart.objects.create(user=user)
        shop_cart.quantity = 1
        shop_cart.save()

    # Check if the item is already in the cart
    try:
        cart_item = CartItem.objects.get(cart=shop_cart, product_color=product)
        cart_item.quantity += quantity
        cart_item.save()
    except CartItem.DoesNotExist:
        # If item is not in cart, create a new cart item
        cart_item = CartItem.objects.create(cart=shop_cart, product_color=product, quantity=quantity,
                                            added_at=timezone.now)

    return Response({"success": "Item added to cart"}, status=status.HTTP_201_CREATED)