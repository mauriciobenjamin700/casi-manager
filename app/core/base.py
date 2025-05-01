from pydantic import BaseModel


class BaseSchema(BaseModel):


    def to_dict(self, exclude: list[str] = [], **kwargs) -> dict:
        """
        Convert the Pydantic model to a dictionary.
        """
        
        data = self.model_dump()

        data = {
            k: v 
            for k, v in data.items() 
            if k is not None and k not in exclude
        }

        data.update(kwargs)

        return data
    
    def from_dict(self, data: dict) -> "BaseSchema":
        """
        Create a Pydantic model from a dictionary.
        """
        
        return self.model_validate(data)